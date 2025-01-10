import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CompareIntegersTest {

    @Test
    public void testEqualIntegers() {
        int a = 50;
        int b = 50;
        int result = compare(a, b);
        assertEquals(1, result, "Expected result is 1 when a and b are equal");
    }

    @Test
    public void testAGreaterThanB() {
        int a = 100;
        int b = 50;
        int result = compare(a, b);
        assertEquals(2, result, "Expected result is 2 when a is greater than b");
    }

    @Test
    public void testBLessThanA() {
        int a = 20;
        int b = 50;
        int result = compare(a, b);
        assertEquals(3, result, "Expected result is 3 when b is greater than a");
    }

    // Helper method to simulate the comparison logic
    private int compare(int a, int b) {
        if (a == b) {
            return 1;
        } else if (a > b) {
            return 2;
        } else {
            return 3;
        }
    }
}