import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CompareIntegersTest {

    @Test
    void testEqualIntegers() {
        int result = CompareIntegers.compareIntegers(10, 10);
        assertEquals(1, result, "Expected result to be 1 when the integers are equal.");
    }

    @Test
    void testFirstIntegerGreater() {
        int result = CompareIntegers.compareIntegers(20, 10);
        assertEquals(2, result, "Expected result to be 2 when the first integer is greater.");
    }

    @Test
    void testSecondIntegerGreater() {
        int result = CompareIntegers.compareIntegers(5, 15);
        assertEquals(3, result, "Expected result to be 3 when the second integer is greater.");
    }

    @Test
    void testNegativeIntegers() {
        int result = CompareIntegers.compareIntegers(-5, -10);
        assertEquals(2, result, "Expected result to be 2 when the first integer is greater, even if negative.");
    }

    @Test
    void testMixedSignIntegers() {
        int result = CompareIntegers.compareIntegers(-5, 10);
        assertEquals(3, result, "Expected result to be 3 when the second integer is greater with mixed signs.");
    }
}
