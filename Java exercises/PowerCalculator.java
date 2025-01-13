/*
Write a program that calculates the power of a base number raised to an exponent using a do while loop. Your output
should be displayed in the following format: '2 raised to the power of 3 is: 8'
 */
public class PowerCalculator {
    public static void main(String[] args) {
        int base = 2;
        int exponent = 0;
        int result = calculatePower(base, exponent);
        System.out.println(base + " raised to the power of " + exponent + " is: " + result);
    }

    /**
     * Calculates the power of a base number raised to a given exponent using a do-while loop.
     * @param base base the base number to be raised to the power
     * @param exponent exponent the exponent to which the base number is raised;
     * @return the result of raising the base to the power of the exponent
     */
    public static int calculatePower(int base, int exponent) {
        if (exponent < 0) {
            throw new IllegalArgumentException("Exponent cannot be negative.");
        }
        int result = 1;
        int count = 0;

        do {
            result *= base;
            count++;
        } while (count < exponent);

        return result;
    }
}
