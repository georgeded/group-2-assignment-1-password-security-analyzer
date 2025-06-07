import unittest
from src.password_check import has_sequential_chars

class TestHasSequentialChars(unittest.TestCase):

    def test_sequential_letters_true(self):
        self.assertTrue(has_sequential_chars("abcd"))

    def test_sequential_digits_true(self):
        self.assertTrue(has_sequential_chars("1234"))

    def test_no_sequence_false(self):
        self.assertFalse(has_sequential_chars("a1b2c3"))

    def test_short_input_false(self):
        self.assertFalse(has_sequential_chars("ab"))

    def test_sequence_in_middle_true(self):
        self.assertTrue(has_sequential_chars("xxabcdxx"))

    def test_custom_seq_len_true(self):
        self.assertTrue(has_sequential_chars("abc", seq_len=3))

    def test_custom_seq_len_false(self):
        self.assertFalse(has_sequential_chars("ab", seq_len=3))

    def test_digits_sequence_with_letters(self):
        self.assertTrue(has_sequential_chars("a1234z"))

    def test_mixed_but_ordered_letters(self):
        self.assertTrue(has_sequential_chars("lmno"))

if __name__ == "__main__":
    unittest.main()