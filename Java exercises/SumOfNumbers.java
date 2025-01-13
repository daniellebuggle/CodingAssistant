/*
Write a program that calculates the sum of all numbers in a given list.
Your output should be displayed in the following format: 'The sum of the list of numbers is: 62'
 */
public class SumOfNumbers {
    public static void main(String[] args) {
        int[] numbers = { 3, 5, 23, 6, 5, 1, 2, 9, 8 };
        int totalSum = calculateSum(numbers);
        System.out.println("The sum of the list of numbers is: " + totalSum);
    }

    /**
     * Calculates the sum of all numbers in the given list.
     * @param numbers an array of integers whose sum is to be calculated
     * @return the sum of all numbers in the array
     */
    public static int calculateSum(int[] numbers) {
        int totalSum = 0;
        for (int i = 0; i < numbers.length; i++) {
            totalSum += numbers[i];
        }
        return totalSum;
    }
}
