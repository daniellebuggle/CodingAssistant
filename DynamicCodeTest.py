import subprocess


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
            "-d", output_dir,  # Specify the output directory for compiled .class files
            f"{source_dir}/{class_name}.java",  # Path to the Java source file
            f"{test_dir}/{test_file}",  # Path to the Java source file
        ]
        subprocess.run(compile_command, check=True)

        # Step 3: Run the JUnit tests
        # Step 3: Run the JUnit tests
        test_command = [
            "java",
            "-jar",
            junit_jar,
            "--classpath",
            f".:{output_dir}",  # Include the directory with the compiled .class files
            "--select-class",
            f"{class_name}Test"  # Target the specific test class
        ]

        # Run the test command
        result = subprocess.run(test_command, capture_output=True, text=True)

        # Step 4: Return the test results
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error occurred: {e}"
    except Exception as ex:
        return f"Unexpected error: {ex}"
