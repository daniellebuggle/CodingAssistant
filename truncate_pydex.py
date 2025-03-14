import random
import json
from AST.Python import python_ast as ast


def detect_language(code):
    """Detects if the given code is Java or Python."""
    java_indicators = ["public class", "System.out.println", "import java.", "{", "}", ";"]
    python_indicators = ["def ", "print(", "import ", "elif", ":", "#"]

    java_score = sum(code.count(indicator) for indicator in java_indicators)
    python_score = sum(code.count(indicator) for indicator in python_indicators)

    if java_score > python_score:
        return "Java"
    elif python_score > java_score:
        return "Python"
    else:
        return None  # Unable to confidently determine language


def truncate_response_AI(code, badges):
    language = detect_language(code)
    if not language:
        raise ValueError("Could not determine language of the code")

    lines = code.strip().split("\n")

    # Define language constructs based on language
    language_constructs = {
        'Java': {
            'for': 'Java For-Loop',
            'while': 'Java While-Loop',
            'do': 'Java Do-While',
            'if': 'Java If-Else',
            'or': 'Java OR Operator'
        },
        'Python': {
            'for': 'Python For-Loop',
            'while': 'Python While-Loop',
            'if': 'Python If-Elif',
            'or': 'Python OR Operator'
        }
    }

    if language not in language_constructs:
        raise ValueError("Unsupported language")

    constructs = language_constructs[language]

    # Identify allowed constructs based on badges
    allowed_constructs = {key for key, value in constructs.items() if value in badges}

    # Parse code and filter statements
    filtered_lines = []
    include_block = True  # Flag to determine whether to include lines

    for line in lines:
        stripped_line = line.strip()

        # Check if line starts with a construct keyword
        if any(stripped_line.startswith(keyword) for keyword in constructs):
            # If construct is not allowed, skip it and the following block
            if not any(keyword in allowed_constructs for keyword in stripped_line.split()):
                include_block = False
            else:
                include_block = True

        if include_block:
            filtered_lines.append(line)

    return "\n".join(filtered_lines)


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
        "truncated_solutions": truncate_solutions,
        "reference_solution": reference_solution
    }

    return processed_data


def extract_and_write_truncated_data(input_filename, output_filename):
    with open(input_filename, "r", encoding="utf-8") as infile:
        data = json.load(infile)  # Adjust this if your file is not JSON

    processed_data = process_dataset(data)


    # Write to a new file
    with open(output_filename, "w", encoding="utf-8") as outfile:
        json.dump(processed_data, outfile, indent=4)

    print(f"Extracted data written to {output_filename}")

"""list_of_inputs = ["EvalPydex/2870_pydex.json", "EvalPydex/2872_pydex.json", "EvalPydex/2873_pydex.json",
                   "EvalPydex/2874_pydex.json", "EvalPydex/2875_pydex.json",
                   "EvalPydex/2877_pydex.json", "EvalPydex/2882_pydex.json", "EvalPydex/2920_pydex.json"]

list_of_outputs = ["EvalPydex/2870_truncated.json", "EvalPydex/2872_truncated.json", "EvalPydex/2873_truncated.json",
                 "EvalPydex/2874_truncated.json", "EvalPydex/2875_truncated.json",
                 "EvalPydex/2877_truncated.json", "EvalPydex/2882_truncated.json", "EvalPydex/2920_truncated.json"]

for i in range(len(list_of_inputs)):
    extract_and_write_truncated_data(list_of_inputs[i], list_of_outputs[i])"""