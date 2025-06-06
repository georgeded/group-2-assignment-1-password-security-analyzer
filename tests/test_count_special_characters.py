import unittest
from src.password_check import count_special_characters

class TestCountSpecialCharacters(unittest.TestCase):
    def test_special_chars_present(self):
        self.assertEqual(count_special_characters("abc!@#123"), 3)

    def test_no_special_chars(self):
        self.assertEqual(count_special_characters("abc123"), 0)

    def test_all_special_chars(self):
        self.assertEqual(count_special_characters("!@#$%^"), 6)

    def test_empty_password(self):
        self.assertEqual(count_special_characters(""), 0)

if __name__ == "__main__":
    unittest.main()

