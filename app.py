from flask import Flask, request, jsonify, Response
import json
from openai import OpenAI
import re
import DynamicCodeTest

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


def stream_response(messages):
    try:
        for message in messages:
            # Phrase to check for
            phrase = 'Test the highlighted code.'
            if phrase in message['content']:
                # Extract the code block encompassed in ``` symbols
                code_match = re.search(r'```(?:[a-zA-Z0-9\s/().-]+)?\n(.*?)```', message['content'], re.DOTALL)
                if code_match:
                    raw_code = code_match.group(1)
                    # Only take the code starting from "public class"
                    start_match = re.search(r'(public class.*)', raw_code, re.DOTALL)
                    if start_match:
                        code = start_match.group(1).strip()
                        class_name_match = re.search(r'public class\s+(\w+)', code)
                        if class_name_match:
                            extracted_class_name = class_name_match.group(1)
                            junit_results = DynamicCodeTest.run_java_tests(code, extracted_class_name)
                            print("CODE RESULTS: \n", junit_results)
                            final_message = (f"These are the test results that the student provided, check to see if "
                                             f"they are all correct. If they are, congratulate them and say they "
                                             f"passed all tests. If not, provide a hint as to where they went "
                                             f"wrong by only naming what test(s) failed.\n\n{junit_results}")
                            messages.append({"role": "assistant", "content": final_message})

        # Stream the response from the OpenAI model
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Replace with your model
            messages=messages,
            stream=True  # Enable streaming
        )

        print("Response received:", response)  # Log full response for inspection

        # Iterate over the streamed response
        for chunk in response:
            # Accessing the content directly from the delta
            if hasattr(chunk.choices[0].delta, "content") and chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                print(content, end="")  # Print the chunk content as it arrives

                # Yield the chunk as JSON
                yield json.dumps({"content": content}) + "\n"

    except Exception as e:
        print(f"Error in streaming: {e}")
        error_message = {"content": f"Error streaming response: {str(e)}"}
        yield json.dumps(error_message) + "\n"


@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    data = request.get_json()
    print(json.dumps(data, indent=4))  # Log the incoming request

    messages = data.get("messages", [])
    if not messages:
        return jsonify({"error": "No messages provided"}), 400
    # Add system message if not already present
    if all(msg["role"] != "system" for msg in messages):
        messages.insert(0, SYSTEM_MESSAGE)

    # Return a streaming response in JSON format
    return Response(
        stream_response(messages),
        content_type='application/json',  # This tells the client to expect JSON
        status=200
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, threaded=True)
