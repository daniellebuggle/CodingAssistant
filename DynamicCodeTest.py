import subprocess
import os

# Step 1: Define the Java class code
java_code = """
public class DynamicCode {
    public static int add(int a, int b) {
        return a + b;
    }

    public static int subtract(int a, int b) {
        return a - b;
    }
}
"""

# Step 3: Write the Java class and test class to files
with open("DynamicCode.java", "w") as java_file:
    java_file.write(java_code)


# Step 4: Compile the Java class and test class
subprocess.run(["javac", "-cp", ".:junit-platform-console-standalone-1.11.4.jar", "DynamicCode.java", "CompareIntegersTest.java"], check=True)

# Step 5: Run the JUnit tests
result = subprocess.run(
    [
        "java",
        "-jar",
        "junit-platform-console-standalone-1.11.4.jar",
        "--classpath",
        ".",
        "--scan-classpath"
    ],
    capture_output=True,
    text=True
)

# Step 6: Print the JUnit test results
print(result.stdout)
