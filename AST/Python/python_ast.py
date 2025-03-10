import ast

badge_mapping = {
    "Python While-Loop": "while",
    "Python For-Loop": "for",
    "Python If-Elif": "if",
    "Python OR Operator": "or"
}


def run_python_ast(code_submission, badge):
    stmnt = badge_mapping.get(badge, "No Badge")
    if not stmnt == "No Badge":
        return contains_statement(code_submission, stmnt)


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


def get_statement_start_line(code_submission, statement_type):
    """
    Returns the line number where a specific statement starts.

    :param code_submission: The source code as a string
    :param statement_type: The type of statement to check for
    :return: The line number of the statement if found, None otherwise
    """
    tree = ast.parse(code_submission)

    for node in ast.walk(tree):
        if isinstance(node, ast.stmt):  # Check only statement nodes
            if hasattr(node, 'lineno'):  # Ensure the node has a line number
                line_number = node.lineno

                if statement_type == 'while' and isinstance(node, ast.While):
                    return line_number
                elif statement_type == 'if' and isinstance(node, ast.If):
                    return line_number
                elif statement_type == 'for' and isinstance(node, ast.For):
                    return line_number
                elif statement_type == 'or' and isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
                    return line_number
    return None  # Return None if the statement type is not found
