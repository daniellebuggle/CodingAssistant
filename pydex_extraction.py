import json


def extract_and_write_data(input_filename, output_filename):
    with open(input_filename, "r", encoding="utf-8") as infile:
        data = json.load(infile)  # Adjust this if your file is not JSON

    extracted_data = {
        "problem_ID": data.get("problem_ID"),
        "statement": data.get("statement"),
        "IO_example": data.get("IO_example"),
        "reference_solution": data.get("reference_solution")
    }

    # Write to a new file
    with open(output_filename, "w", encoding="utf-8") as outfile:
        json.dump(extracted_data, outfile, indent=4)

    print(f"Extracted data written to {output_filename}")


list_of_inputs = ["PyDex/2870_syntaxincorrect_correct_pair.json", "PyDex/2872_syntaxincorrect_correct_pair.json",
                  "PyDex/2873_syntaxincorrect_correct_pair.json", "PyDex/2874_syntaxincorrect_correct_pair.json",
                  "PyDex/2875_syntaxincorrect_correct_pair.json", "PyDex/2877_syntaxincorrect_correct_pair.json",
                  "PyDex/2882_syntaxincorrect_correct_pair.json", "PyDex/2920_syntaxincorrect_correct_pair.json"]

list_of_outputs = ["EvalPydex/2870_pydex.json", "EvalPydex/2872_pydex.json", "EvalPydex/2873_pydex.json",
                   "EvalPydex/2874_pydex.json", "EvalPydex/2875_pydex.json",
                   "EvalPydex/2877_pydex.json", "EvalPydex/2882_pydex.json", "EvalPydex/2920_pydex.json"]

for i in range(len(list_of_inputs)):
    extract_and_write_data(list_of_inputs[i], list_of_outputs[i])

