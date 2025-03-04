from flask import Flask, request, jsonify, Response
import json
from openai import OpenAI
import re
import exercises_badges, database, DynamicCodeTest
from AST.Java import java_ast
from AST.Python import python_ast

app = Flask(__name__)
client = OpenAI()

# Default system message for the AI assistant
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are a helpful coding assistant who will provide code answers to the user. "
               "You do not offer explanations with the code. Just give a code answer. If the user "
               "asks a question unrelated to generating a coding answer, respond by telling the user, "
               "\"I can't help you with that, sorry\"."
}


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
        for message in messages:
            # Phrase to check for
            phrase = 'Test the highlighted code.'
            if phrase in message['content']:
                # Extract the code block within ``` symbols
                code_match = re.search(r'```(?:[^\n]*)?\n(.*?)```', message['content'], re.DOTALL)
                if code_match:
                    raw_code = code_match.group(1)
                    ast_results = False
                    # Process code
                    if "public class" in raw_code:
                        student_exercise, java_results = process_code(raw_code, "java")
                        results = java_results
                        badge = exercises_badges.check_badge(student_exercise)
                        ast_results = java_ast.run_java_ast(raw_code, badge)
                        database.assign_badge_if_tests_passed(1, badge, results, "java", ast_results)
                    elif "def " in raw_code:
                        student_exercise, python_results = process_code(raw_code, "python")
                        results = python_results
                        badge = exercises_badges.check_badge(student_exercise)
                        ast_results = python_ast.run_python_ast(raw_code, badge)
                        database.assign_badge_if_tests_passed(1, badge, results, "python",
                                                              ast_results)
                    else:
                        print("No valid code detected.")

                    if ast_results:
                        final_message = (
                            f"These are the test results to the code that the student provided. Check to see if "
                            f"they are all correct. Only if ALL TESTS are correct, you should congratulate them and say "
                            f"they passed all tests, and let them know they earned the {badge} badge. If they failed any"
                            f" test, provide a hint as to where they went wrong by only naming what test(s) failed."
                            f"\n\n{results}"
                        )
                    else:
                        final_message = (
                            f"DO NOT CONGRATULATE THE USER. These are the test results to the code that the student "
                            f"provided. Check to see if they are all correct. If they are say they passed all of the "
                            f"unit tests but they failed to use the coding concept to earn the {badge} badge. If they "
                            f"failed any test, provide a hint as to where they went wrong by only naming what test(s) "
                            f"failed."
                            f"\n\n{results}"
                        )
                    messages.append({"role": "assistant", "content": final_message})

        # Stream the response from the OpenAI model
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True  # Enable streaming
        )

        # print(response)
        # Iterate over the streamed response
        for chunk in response:
            if hasattr(chunk.choices[0].delta, "content") and chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                print(content, end="")
                yield json.dumps({"content": content}) + "\n"

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

    print(json.dumps(messages, indent=4))

    # Return a streaming response in JSON format
    return Response(
        stream_response(messages),
        content_type='application/json',
        status=200
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, threaded=True)
