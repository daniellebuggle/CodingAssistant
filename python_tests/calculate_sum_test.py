import unittest
class calculate_sum_test(unittest.TestCase):
    def test_positive_numbers(self):
        """Test a list of positive numbers."""
        self.assertEqual(calculate_sum([3, 5, 23, 6, 5, 1, 2, 9, 8]), 62)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(calculate_sum([-3, -5, -2, -7]), -17)

    def test_mixed_numbers(self):
        """Test a list with both positive and negative numbers."""
        self.assertEqual(calculate_sum([10, -5, 3, -8, 0]), 0)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(calculate_sum([]), 0)

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(calculate_sum([42]), 42)

    def test_zeros(self):
        """Test a list with all zeros."""
        self.assertEqual(calculate_sum([0, 0, 0, 0]), 0)