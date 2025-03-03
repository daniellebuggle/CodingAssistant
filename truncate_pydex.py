import random
import json
from AST.Python import python_ast as ast


def truncate_solution(solution, strategy):
    """
    Truncate the given solution based on the specified strategy.

    :param solution: String of the example solution
    :param strategy: One of the following
        - "early": Truncate after variable initialisation.
        - "midway": Truncate after key logic setup (e.g., loop, condition setup).
        - "late": Truncate just before final output.
        - "random": Randomly pick a truncation point.
    :return: Truncated solution at strategy point
    """
    lines = solution.strip().split("\n")

    if strategy == "midway":
        # Check for the first occurrence of key statements
        for statement in ['while', 'if', 'for', 'or']:
            line_number = ast.get_statement_start_line(solution, statement)
            if line_number:
                truncation_point = line_number - 1  # Truncate just before the statement line
                truncated_solution = "\n".join(lines[:truncation_point])
                return truncated_solution

    truncation_points = {
        "early": 2,  # After variable initialization
        "late": len(lines) - 1,  # Just before final print
    }

    if strategy == "random":
        truncation_point = random.choice(list(truncation_points.values()))
    else:
        truncation_point = truncation_points.get(strategy, len(lines))

    truncated_solution = "\n".join(lines[:truncation_point])
    return truncated_solution


def process_dataset(dataset):
    """
    Process dataset and apply truncation strategies to the reference solution.
    :param dataset: JSON file with PyDex data.
    :return: Processed data with multiple truncated solutions.
    """
    reference_solution = dataset.get("reference_solution")
    strategies = ["early", "midway", "late"]
    truncate_solutions = []
    for strat in strategies:
        truncated_sol = truncate_solution(reference_solution, strat)
        truncate_solutions.append(truncated_sol)

    processed_data = {
        "problem_ID": dataset.get("problem_ID"),
        "statement": dataset.get("statement"),
        "IO_example": dataset.get("IO_example"),
        "truncated_solutions": truncate_solutions
    }

    return processed_data


list_of_inputs = ["EvalPydex/2870_pydex.json", "EvalPydex/2872_pydex.json",
                  "EvalPydex/2873_pydex.json", "EvalPydex/2874_pydex.json",
                  "EvalPydex/2875_pydex.json", "EvalPydex/2877_pydex.json",
                  "EvalPydex/2882_pydex.json", "EvalPydex/2920_pydex.json"]

list_of_outputs = ["EvalPydex/2870_truncated.json", "EvalPydex/2872_truncated.json", "EvalPydex/2873_truncated.json",
                   "EvalPydex/2874_truncated.json", "EvalPydex/2875_truncated.json",
                   "EvalPydex/2877_truncated.json", "EvalPydex/2882_truncated.json", "EvalPydex/2920_truncated.json"]

for i in range(len(list_of_inputs)):
    with open(list_of_inputs[i], "r") as f:
        dataset = json.load(f)

    truncated_data = process_dataset(dataset)

    with open(list_of_outputs[i], "w") as f:
        json.dump(truncated_data, f, indent=4)
