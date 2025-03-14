from dotenv import load_dotenv
from openai import OpenAI
import restrict_responses as r
from AST.Python.python_ast import *
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

output_files = ["Evaluation/zero_shot/2870_responses.json", "Evaluation/zero_shot/2872_responses.json",
                "Evaluation/zero_shot/2873_responses.json",
                "Evaluation/zero_shot/2874_responses.json", "Evaluation/zero_shot/2875_responses.json",
                "Evaluation/zero_shot/2877_responses.json", "Evaluation/zero_shot/2882_responses.json",
                "Evaluation/zero_shot/2920_responses.json"]

cot_few_shot_output = ["Evaluation/cot_few_shot/2870_responses.json", "Evaluation/cot_few_shot/2872_responses.json",
                       "Evaluation/cot_few_shot/2873_responses.json",
                       "Evaluation/cot_few_shot/2874_responses.json", "Evaluation/cot_few_shot/2875_responses.json",
                       "Evaluation/cot_few_shot/2877_responses.json", "Evaluation/cot_few_shot/2882_responses.json",
                       "Evaluation/cot_few_shot/2920_responses.json"]
STUDENT_ID = 1


# TODO: Get lists of various output files for different runs with different lists of badges

def run_evaluate_script(constraint_prompt, example_badges, outputs, ):
    for file, output_file in zip(list_of_files, outputs):
        with open(file) as f:
            data = json.load(f)
            problem_id = data["problem_ID"]
            statement = data["statement"]
            truncated_solutions = data["truncated_solutions"]
            opt_solution = data["reference_solution"]

            simulated_students = []
            for trunc_sol in truncated_solutions:
                messages = []
                messages.insert(0, SYSTEM_MESSAGE)
                simulated_student_question = statement + "\n This is the code I have written so far. \n" + trunc_sol

                badges = example_badges
                # TODO: Switch statements to indicate what prompt is being evaluated using constraint_prompt as a #
                match constraint_prompt:
                    case 1:
                        prompt_to_restrict = r.cot_few_shot_general_query(badges, simulated_student_question)
                    case 2:
                        prompt_to_restrict = r.zero_shot_prompt_general_query(badges, simulated_student_question)
                    case 3:
                        prompt_to_restrict = r.zero_shot_prompt_general_query(badges, simulated_student_question)
                    case _:
                        prompt_to_restrict = r.zero_shot_prompt_general_query(badges, simulated_student_question)

                messages.append({"role": "assistant", "content": prompt_to_restrict})

                messages.append({"role": "user", "content": simulated_student_question})
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages,
                    stream=False  # Enable streaming
                )

                incorrect = False
                incorrect_guardrail = False
                ai_response = response.choices[0].message.content
                if "```" in ai_response:
                    truncate_AI = truncate_response_AI(ai_response, badges)
                    AST_guardrail_response = json.dumps({"content": truncate_AI}) + "\n"

                    # Check if values are correct or incorrect for AI response
                    used_constructs = []
                    for badge, keyword in badge_mapping.items():
                        if contains_statement(ai_response.strip('```python\n').strip('```'), keyword):
                            used_constructs.append(keyword)
                            if badge not in badges:
                                incorrect = True

                    # repeat for guardrail response
                    used_constructs = []
                    for badge, keyword in badge_mapping.items():
                        if contains_statement(AST_guardrail_response.strip('```python\n').strip('```'), keyword):
                            used_constructs.append(keyword)
                            if badge not in badges:
                                incorrect_guardrail = True
                else:
                    AST_guardrail_response = ai_response

                    # If response is not code then check optimal solution and compare to badges for correct/incorrect
                    used_constructs = []
                    for badge, keyword in badge_mapping.items():
                        if contains_statement(opt_solution, keyword):
                            used_constructs.append(keyword)
                            if badge in badges:  # If it is in badges - restricted response for no reason
                                incorrect = True
                                incorrect_guardrail = True

                simulated_students.append({
                    "question": simulated_student_question,
                    "student_code": trunc_sol,
                    "ai_response": ai_response,
                    "AST_guardrail_response": AST_guardrail_response,
                    "ai_status": "Incorrect" if incorrect else "Correct",
                    "ast_guardrail_status": "Incorrect" if incorrect_guardrail else "Correct"
                })

            result = {
                "problem_ID": problem_id,
                "statement": statement,
                "list_of_badges": badges,
                "simulated_students": simulated_students
            }

        with open(output_file, "w") as outfile:
            json.dump(result, outfile, indent=4)


def evaluate_status(files, output_file):
    results = {
        "ai_status": {"correct": 0, "incorrect": 0},
        "ast_guardrail_status": {"correct": 0, "incorrect": 0}
    }

    for file in files:
        with open(file, "r") as f:
            data = json.load(f)

            for student in data.get("simulated_students", []):
                ai_status = student.get("ai_status", "Incorrect")
                ast_status = student.get("ast_guardrail_status", "Incorrect")

                if ai_status == "Correct":
                    results["ai_status"]["correct"] += 1
                else:
                    results["ai_status"]["incorrect"] += 1

                if ast_status == "Correct":
                    results["ast_guardrail_status"]["correct"] += 1
                else:
                    results["ast_guardrail_status"]["incorrect"] += 1
    with open(output_file, "w") as out_f:
        json.dump(results, out_f, indent=4)

    return results


# Example usage
summary = evaluate_status(cot_few_shot_output, "Evaluation/cot_few_shot/overall_numbers.json")
print(summary)
summary = evaluate_status(output_files, "Evaluation/zero_shot/overall_numbers.json")
print(summary)

#run_evaluate_script(0, ['Python For-Loop'], output_files)
#run_evaluate_script(1, ['Python For-Loop', 'Python While Loop'], cot_few_shot_output)
