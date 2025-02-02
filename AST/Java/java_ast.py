import subprocess
import os

java_file = "AST/Java/ASTParser.java"
output_dir = "AST/Java/out/"
javaparser_jar = "lib/javaparser-core-3.26.3.jar"
class_file = "AST/Java/out/ASTParser.class"


def compile_java_ast():
    compile_command = [
        "javac", "-cp", f"{javaparser_jar}", java_file, "-d", output_dir, java_file
    ]
    subprocess.run(compile_command, check=True)


def run_java_ast(submitted_code, badge_type):
    if not os.path.exists(class_file):
        compile_java_ast()

    command = ["java", "-cp", f"{javaparser_jar}:{output_dir}", "ASTParser", submitted_code, badge_type]

    result = subprocess.run(command, capture_output=True, text=True)

    print(result)

    if result.returncode == 0:  # Check if the command ran successfully
        output = result.stdout.strip()  # Get the standard output from the command

        if f"The code contains a {badge_type} statement." in output:
            return True
        elif f"The code does not contain a {badge_type} statement." in output:
            return False
        else:
            print("Unexpected output:", output)
            return None  # Return None if the output is not as expected
    else:
        print("Error running the Java command:", result.stderr)
        return None
