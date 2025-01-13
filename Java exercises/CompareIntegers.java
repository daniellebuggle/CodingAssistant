/*
Write a program that compares two integers, a and b. Set a variable
'result' to:
    1 if a and b are equal
    2 if a is greater than b, or
    3 if b is greater than a
 */

public class CompareIntegers {
    public static void main(String[] args) {
        int a = 100; // You can change these values to test different cases
        int b = 44;
        int result = compareIntegers(a, b);
        System.out.println(result);
    }

    /**
     * Compares two integers.
     * @param a the first integer to compare
     * @param b the second integer to compare
     * @return 1 if a == b, 2 if a > b, 3 if a < b
     */
    public static int compareIntegers(int a, int b) {
        if (a == b) {
            return 1;
        } else if (a > b) {
            return 2;
        } else {
            return 3;
        }
    }
}
