import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PowerCalculatorTest {

    @Test
    public void testPowerOfZeroExponent() {
        // Any number raised to the power of 0 is 1
        assertEquals(1, PowerCalculator.calculatePower(2, 0));
        assertEquals(1, PowerCalculator.calculatePower(10, 0));
    }

    @Test
    public void testPowerOfZeroBase() {
        // 0 raised to any positive power is 0
        assertEquals(0, PowerCalculator.calculatePower(0, 5));
    }

    @Test
    public void testPowerOfPositiveBaseAndExponent() {
        // 2^3 = 8
        assertEquals(8, PowerCalculator.calculatePower(2, 3));
        // 3^4 = 81
        assertEquals(81, PowerCalculator.calculatePower(3, 4));
    }

    @Test
    public void testPowerOfOneBase() {
        // 1 raised to any power is 1
        assertEquals(1, PowerCalculator.calculatePower(1, 5));
        assertEquals(1, PowerCalculator.calculatePower(1, 10));
    }

    @Test
    public void testPowerOfNegativeBaseEvenExponent() {
        // (-2)^2 = 4
        assertEquals(4, PowerCalculator.calculatePower(-2, 2));
    }

    @Test
    public void testPowerOfNegativeBaseOddExponent() {
        // (-2)^3 = -8
        assertEquals(-8, PowerCalculator.calculatePower(-2, 3));
    }

    @Test
    public void testNegativeExponentThrowsException() {
        // Negative exponents should throw an exception
        assertThrows(IllegalArgumentException.class, () -> PowerCalculator.calculatePower(2, -3));
    }
}
