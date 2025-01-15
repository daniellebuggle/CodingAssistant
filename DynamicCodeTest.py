import importlib
import subprocess
import unittest
import io


def run_python_tests(code, function_name):
    """
    Executes python function and runs its corresponding unit tests.
    :param code: str
        Python source code as a string, with the function to be tested.
    :param function_name: str
        Name of the function to test.
    :return: str
        Results of the test suite execution.
    """
    namespace = {}
    exec(code, namespace)

    # Retrieve the function from the executed code
    dynamic_function = namespace.get(function_name)

    if not dynamic_function:
        raise ValueError(f"Function '{function_name}' not found in the provided code.")

    try:
        module_name = f"python_tests.{function_name}Test"
        module = importlib.import_module(module_name)
    except ImportError as e:
        raise ValueError(
            f"Test module for '{function_name}' could not be imported. Ensure the file exists in the 'Test' folder.") \
            from e

    # Set attributes so that dynamic_function can be used in the test suite
    setattr(module, function_name, dynamic_function)
    test_class = getattr(module, f"{function_name}Test", None)
    if not test_class:
        raise ValueError(f"Test class for function '{function_name}' not found in the test module.")

    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    buffer = io.StringIO()
    runner = unittest.TextTestRunner(stream=buffer, verbosity=2)
    runner.run(suite)

    return buffer.getvalue()


def run_java_tests(code, class_name):
    """
    Compiles and runs Java code with JUnit tests.

    Parameters:
        code (str): The Java code to write to a file.
        class_name (str): The name of the class submitted to be tested.
        test_file (str): The name of the JUnit test file.

    Returns:
        str: The output of the JUnit test results.
    """
    try:
        source_dir = "src"
        output_dir = "out"
        test_dir = "test"

        test_file = f"{class_name}Test.java"
        junit_jar = "junit-platform-console-standalone-1.11.4.jar"

        # Step 1: Write the Java class to a file
        with open(f"src/{class_name}.java", "w") as java_file:
            java_file.write(code)

        # Step 2: Compile the Java class and test class
        compile_command = [
            "javac",
            "-cp",
            f".:{junit_jar}",
            "-d", output_dir,
            f"{source_dir}/{class_name}.java",
            f"{test_dir}/{test_file}",
        ]
        subprocess.run(compile_command, check=True)

        # Step 3: Run the JUnit tests
        test_command = [
            "java",
            "-jar",
            junit_jar,
            "--classpath",
            f".:{output_dir}",
            "--select-class",
            f"{class_name}Test"
        ]

        result = subprocess.run(test_command, capture_output=True, text=True)

        # Step 4: Return the test results
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error occurred: {e}"
    except Exception as ex:
        return f"Unexpected error: {ex}"
