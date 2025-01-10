import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class FactorialCalculatorTest {

    @Test
    public void testFactorialOfZero() {
        // Factorial of 0 is 1
        assertEquals(1, FactorialCalculator.calculateFactorial(0));
    }

    @Test
    public void testFactorialOfPositiveNumber() {
        // Factorial of 5 is 120
        assertEquals(120, FactorialCalculator.calculateFactorial(5));
    }

    @Test
    public void testFactorialOfOne() {
        // Factorial of 1 is 1
        assertEquals(1, FactorialCalculator.calculateFactorial(1));
    }

    @Test
    public void testFactorialOfLargeNumber() {
        // Factorial of 10 is 3,628,800
        assertEquals(3628800, FactorialCalculator.calculateFactorial(10));
    }

    @Test
    public void testFactorialOfNegativeNumber() {
        // Factorial is not defined for negative numbers, so we can throw an exception.
        // Alternatively, we can return -1 or handle the case as per requirements.
        assertThrows(IllegalArgumentException.class, () -> FactorialCalculator.calculateFactorial(-5));
    }
}
