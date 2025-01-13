import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class SumOfNumbersTest {

    @Test
    public void testSumOfPositiveNumbers() {
        int[] numbers = {3, 5, 23, 6, 5, 1, 2, 9, 8};
        assertEquals(62, SumOfNumbers.calculateSum(numbers));
    }

    @Test
    public void testSumOfNegativeNumbers() {
        int[] numbers = {-3, -5, -10, -7};
        assertEquals(-25, SumOfNumbers.calculateSum(numbers));
    }

    @Test
    public void testSumOfMixedNumbers() {
        int[] numbers = {3, -5, 10, -7};
        assertEquals(1, SumOfNumbers.calculateSum(numbers));
    }

    @Test
    public void testSumOfEmptyArray() {
        int[] numbers = {};
        assertEquals(0, SumOfNumbers.calculateSum(numbers));
    }

    @Test
    public void testSumOfSingleElementArray() {
        int[] numbers = {42};
        assertEquals(42, SumOfNumbers.calculateSum(numbers));
    }

    @Test
    public void testSumOfAllZeroes() {
        int[] numbers = {0, 0, 0, 0};
        assertEquals(0, SumOfNumbers.calculateSum(numbers));
    }
}
