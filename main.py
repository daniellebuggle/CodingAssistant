from openai import OpenAI

client = OpenAI()

messages = [
    {"role": "system",
     "content": "You are a helpful coding assistant who will provide code answers to the user. "
                "You do not offer explanations with the code. Just give a code answer. If the user "
                "asks a question unrelated to generating a coding answer, respond by telling the user "
                "\"I can't help you with that, sorry\"."
    }
]

exit_loop = False
while not exit_loop:
    print("You: ")
    user_input = input()
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Conversation is finished.")
        exit_loop = True
    else:
        messages.append({"role": "user", "content": user_input})

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        response = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": response})
        print("AI:", response)
