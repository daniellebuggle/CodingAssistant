/*
Write a program that calculates the factorial of a given number n using a while loop.
*/

public class FactorialCalculator {
    public static void main(String[] args) {
        int n = 5;
        int factorial = calculateFactorial(n);
        System.out.println("The factorial of " + n + " is: " + factorial);
    }

    /**
     * Calculates the factorial of a given natural number.
     * @param n the natural number for which the factorial is to be calculated
     * @return the factorial of the given number
     */
    public static int calculateFactorial(int n) {
        int factorial = 1;
        int i = 1;
        while (i <= n) {
            factorial *= i;
            i++;
        }
        return factorial;
    }
}
