import unittest
class compare_integers_test(unittest.TestCase):
    def test_equal(self):
        """Check when both integers are equal."""
        self.assertEqual(compare_integers(10, 10), 1)  # a == b

    def test_a_greater(self):
        """Check when the first integer is greater."""
        self.assertEqual(compare_integers(20, 10), 2)  # a > b

    def test_b_greater(self):
        """Check when the second integer is greater."""
        self.assertEqual(compare_integers(5, 15), 3)  # b > a