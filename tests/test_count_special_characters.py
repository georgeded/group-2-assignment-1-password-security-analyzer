import unittest
from src.password_check import count_special_characters

class TestCountSpecialCharacters(unittest.TestCase):
    def test_special_chars_present(self):
        # “abc!@#123” has exactly 3 special characters: !, @, #
        self.assertEqual(count_special_characters("abc!@#123"), 3)

    def test_no_special_chars(self):
        # “abc123” has zero special characters
        self.assertEqual(count_special_characters("abc123"), 0)

    def test_all_special_chars(self):
        # “!@#$%^” has 6 special characters
        self.assertEqual(count_special_characters("!@#$%^"), 6)

    def test_empty_password(self):
        # An empty string should return 0
        self.assertEqual(count_special_characters(""), 0)

if __name__ == "__main__":
    unittest.main()

