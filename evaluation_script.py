from dotenv import load_dotenv
from openai import OpenAI
import restrict_responses as r
from truncate_pydex import *

load_dotenv()
client = OpenAI()
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are a helpful coding assistant who will provide code answers to the user. "
               "You do not offer explanations with the code. Just give a code answer. If the user "
               "asks a question unrelated to generating a coding answer, respond by telling the user, "
               "\"I can't help you with that, sorry\". You may answer questions about what badges the student knows."
}

list_of_files = ["EvalPydex/2870_truncated.json", "EvalPydex/2872_truncated.json", "EvalPydex/2873_truncated.json",
                 "EvalPydex/2874_truncated.json", "EvalPydex/2875_truncated.json",
                 "EvalPydex/2877_truncated.json", "EvalPydex/2882_truncated.json", "EvalPydex/2920_truncated.json"]

output_files = ["Evaluation/2870_responses.json", "Evaluation/2872_responses.json", "Evaluation/2873_responses.json",
                "Evaluation/2874_responses.json", "Evaluation/2875_responses.json",
                "Evaluation/2877_responses.json", "Evaluation/2882_responses.json", "Evaluation/2920_responses.json"]

STUDENT_ID = 1


# TODO: Get lists of various output files for different runs with different lists of badges
def run_evaluate_script(constraint_prompt, example_badges, outputs, ):
    for file, output_file in zip(list_of_files, outputs):
        with open(file) as f:
            data = json.load(f)
            problem_id = data["problem_ID"]
            statement = data["statement"]
            truncated_solutions = data["truncated_solutions"]

            simulated_students = []
            for trunc_sol in truncated_solutions:
                messages = []
                messages.insert(0, SYSTEM_MESSAGE)
                simulated_student_question = statement + "\n This is the code I have written so far. \n" + trunc_sol

                badges = example_badges
                # TODO: Switch statements to indicate what prompt is being evaluated using constraint_prompt as a #
                prompt_to_restrict = r.zero_shot_prompt_general_query(badges, simulated_student_question)
                messages.append({"role": "assistant", "content": prompt_to_restrict})

                messages.append({"role": "user", "content": simulated_student_question})
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages,
                    stream=False  # Enable streaming
                )

                ai_response = response.choices[0].message.content

                truncate_AI = truncate_response_AI(ai_response, badges)
                AST_guardrail_response = json.dumps({"content": truncate_AI}) + "\n"

                simulated_students.append({
                    "question": simulated_student_question,
                    "student_code": trunc_sol,
                    "ai_response": ai_response,
                    "AST_guardrail_response": AST_guardrail_response
                })

            result = {
                "problem_ID": problem_id,
                "statement": statement,
                "list_of_badges": badges,
                "simulated_students": simulated_students
            }

        with open(output_file, "w") as outfile:
            json.dump(result, outfile, indent=4)


run_evaluate_script(1, ['Python For-Loop'], output_files)
