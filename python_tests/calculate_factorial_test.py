import unittest

class calculate_factorial_test(unittest.TestCase):
    def test_factorial_zero(self):
        """Test the factorial of 0 (special case)."""
        self.assertEqual(calculate_factorial(0), 1)

    def test_factorial_one(self):
        """Test the factorial of 1."""
        self.assertEqual(calculate_factorial(1), 1)

    def test_factorial_positive(self):
        """Test the factorial of a positive number."""
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(3), 6)

    def test_factorial_large(self):
        """Test the factorial of a larger number."""
        self.assertEqual(calculate_factorial(10), 3628800)

    def test_negative_number(self):
        """Test that a negative number raises a ValueError."""
        with self.assertRaises(ValueError):
            calculate_factorial(-5)

if __name__ == "__main__":
    unittest.main()
