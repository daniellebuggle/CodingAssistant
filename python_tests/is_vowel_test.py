import unittest

class is_vowel_test(unittest.TestCase):
    def test_vowel_lowercase(self):
        """Test lowercase vowels."""
        self.assertTrue(is_vowel('a'))
        self.assertTrue(is_vowel('e'))
        self.assertTrue(is_vowel('i'))
        self.assertTrue(is_vowel('o'))
        self.assertTrue(is_vowel('u'))

    def test_vowel_uppercase(self):
        """Test uppercase vowels."""
        self.assertTrue(is_vowel('A'))
        self.assertTrue(is_vowel('E'))
        self.assertTrue(is_vowel('I'))
        self.assertTrue(is_vowel('O'))
        self.assertTrue(is_vowel('U'))

    def test_consonants(self):
        """Test consonants."""
        self.assertFalse(is_vowel('b'))
        self.assertFalse(is_vowel('z'))
        self.assertFalse(is_vowel('x'))

    def test_non_alphabetic(self):
        """Test non-alphabetic characters."""
        self.assertFalse(is_vowel('1'))
        self.assertFalse(is_vowel('@'))
        self.assertFalse(is_vowel(' '))

    def test_empty_string(self):
        """Test empty string."""
        self.assertFalse(is_vowel(''))

if __name__ == "__main__":
    unittest.main()
