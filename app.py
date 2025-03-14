from flask import Flask, request, jsonify, Response
from openai import OpenAI
import re
import exercises_badges, database, DynamicCodeTest
from AST.Java import java_ast
from AST.Python import python_ast
import test_result_feedback as tf
import restrict_responses as r
from truncate_pydex import *

app = Flask(__name__)
client = OpenAI()

# Default system message for the AI assistant
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are a helpful coding assistant who will provide code answers to the user. "
               "You do not offer explanations with the code. Just give a code answer. If the user "
               "asks a question unrelated to generating a coding answer, respond by telling the user, "
               "\"I can't help you with that, sorry\". You may answer questions about what badges the student knows."
}

STUDENT_ID = 1


def process_code(raw_code, language):
    if language == "java":
        code_match = re.search(r'(public class.*)', raw_code, re.DOTALL)
        if code_match:
            code = code_match.group(1).strip()
            class_name_match = re.search(r'public class\s+(\w+)', code)
            if class_name_match:
                class_name = class_name_match.group(1)
                test_results = DynamicCodeTest.run_java_tests(code, class_name)
                return class_name, test_results

    elif language == "python":
        code_match = re.search(r'(def.*)', raw_code, re.DOTALL)
        if code_match:
            code = code_match.group(1).strip()
            function_name_match = re.search(r'def\s+(\w+)', code)
            if function_name_match:
                function_name = function_name_match.group(1)
                test_results = DynamicCodeTest.run_python_tests(code, function_name)
                return function_name, test_results
    return None, None


def stream_response(messages):
    try:
        last_message = messages[-1] if messages else None
        # Phrase to check for
        code_phrase = 'Test the highlighted code.'
        json_phrase = 'Export the current chat session to JSON format.'
        if code_phrase in last_message['content']:
            # Extract the code block within ``` symbols
            code_match = re.search(r'```(?:[^\n]*)?\n(.*?)```', last_message['content'], re.DOTALL)
            if code_match:
                raw_code = code_match.group(1)
                ast_results = False
                # Process code
                if "public class" in raw_code:
                    student_exercise, java_results = process_code(raw_code, "java")
                    results = java_results
                    badge = exercises_badges.check_badge(student_exercise)
                    ast_results = java_ast.run_java_ast(raw_code, badge)
                    database.assign_badge_if_tests_passed(STUDENT_ID, badge, results, "java", ast_results)
                elif "def " in raw_code:
                    student_exercise, python_results = process_code(raw_code, "python")
                    results = python_results
                    badge = exercises_badges.check_badge(student_exercise)
                    ast_results = python_ast.run_python_ast(raw_code, badge)
                    database.assign_badge_if_tests_passed(STUDENT_ID, badge, results, "python",
                                                          ast_results)
                else:
                    print("No valid code detected.")

                ast_prompt = f"AST Test Results:\n {ast_results}"
                # final_message = tf.provide_few_shot_prompt(results, badge, ast_prompt)
                final_message = tf.provide_chain_of_thought_prompt(results, badge, ast_prompt)
                messages.append({"role": "assistant", "content": final_message})
        elif json_phrase in last_message['content']:
            messages.append({"role": "assistant", "content": json_phrase})
        else:
            last_message = messages[-1] if messages else None
            last_message_content = last_message.get("content", "")
            badges = database.get_badges(STUDENT_ID)
            # prompt_to_restrict = r.zero_shot_prompt_general_query(badges, last_message_content)
            # prompt_to_restrict = r.few_shot_prompt_general_query(badges, last_message_content)
            all_badges = exercises_badges.get_all_badges()
            # prompt_to_restrict = r.chain_of_thought_general_query(badges, last_message_content, all_badges)
            coding_concepts_know = r.generate_code(last_message_content, badges)
            messages.append({"role": "assistant", "content": coding_concepts_know})

        badges = database.get_badges(STUDENT_ID)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True  # Enable streaming
        )


        full_content = ""
        for chunk in response:
            if hasattr(chunk.choices[0].delta, "content") and chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_content += content

        # GUARDRAIL USING AST TO RESTRICT AI RESPONSE
        if "```" in full_content:
            truncated = truncate_response_AI(full_content, badges)
            yield json.dumps({"content": truncated}) + "\n"
        else:
            yield json.dumps({"content": full_content}) + "\n"

    except Exception as e:
        print(f"Error in streaming: {e}")
        error_message = {"content": f"Error streaming response: {str(e)}"}
        yield json.dumps(error_message) + "\n"


@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    data = request.get_json()
    messages = data.get("messages", [])
    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    # Add system message if not already present
    messages_to_keep = []

    for msg in messages:
        if not (msg["role"] == "system" and msg["content"] != SYSTEM_MESSAGE["content"]):
            messages_to_keep.append(msg)

    messages = messages_to_keep
    messages.insert(0, SYSTEM_MESSAGE)

    return Response(
        stream_response(messages),
        content_type='application/json',
        status=200
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, threaded=True)
