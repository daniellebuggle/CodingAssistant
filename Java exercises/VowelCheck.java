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
