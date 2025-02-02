import ast


def contains_statement(code_submission, statement_type):
    """
    Checks if the given code contains a specific statement using the AST module.

    :param code_submission: The source code as a string
    :param statement_type: The type of statement to check for
    :return: True if the statement type is found, False otherwise
    """
    tree = ast.parse(code_submission)

    for node in ast.walk(tree):
        if statement_type == 'while' and isinstance(node, ast.While):
            return True
        elif statement_type == 'if' and isinstance(node, ast.If):
            return True
        elif statement_type == 'for' and isinstance(node, ast.For):
            return True
        elif statement_type == 'or' and isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
            return True
    return False


code = """
\"""
Write a Python program that calculates the sum of all numbers in a given list. 
\"""


def calculate_sum(numbers):
    \"""
    Calculates the sum of all numbers in a given list.

    :param numbers: List of numbers to sum up
    :return: The sum of the list
    \"""
    total_sum = 0
    for x in numbers:
        total_sum += x
    return total_sum


def main():
    numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]
    total_sum = calculate_sum(numbers)
    print("The sum of the list of numbers is:", total_sum)


# Run the main function
if __name__ == "__main__":
    main()

"""

print(contains_statement(code, 'for'))
