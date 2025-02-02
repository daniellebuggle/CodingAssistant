import subprocess



java_file = "Java AST/ASTParser.java"
output_dir = "Java AST/out"
javaparser_jar = "javaparser-core-3.26.3.jar"


print("Compiling ASTParser.java...")
compile_command = [
    "javac", "-cp", javaparser_jar, "-d", output_dir, java_file
]
subprocess.run(compile_command, check=True)

java_code = '''
/*
Write a program that checks if a letter is a vowel ('a', 'e', 'i', 'o',
or 'u'). Store your result in a variable called 'output'.
 */
public class VowelCheck {
    public static void main(String[] args) {
        char letter = 'e'; // Change this to test with different letters
        boolean output = isVowel(letter);
        System.out.println(output);
    }

    /**
     * Checks if the given character is a vowel.
     * 
     * @param letter the character to check
     * @return {@code true} if the character is a vowel; {@code false} otherwise
     */
    public static boolean isVowel(char letter) {
        return letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u' ||
                letter == 'A' || letter == 'E' || letter == 'I' || letter == 'O' || letter == 'U';
    }
}

'''

badge_type = "Java OR Operator"

command = ["java", "-cp", f"{javaparser_jar}:{output_dir}", "ASTParser", java_code, badge_type]

result = subprocess.run(command, capture_output=True, text=True)

# Print the output from Java
print("JavaParser Output:\n", result.stdout)
