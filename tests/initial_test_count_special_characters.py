import unittest
from src.password_check import count_special_characters

class TestCountSpecialCharacters(unittest.TestCase):

    def test_no_special_chars(self):
        self.assertEqual(count_special_characters("abc123"), 0)

    def test_empty_password(self):
        self.assertEqual(count_special_characters(""), 0)

if __name__ == "__main__":
    unittest.main()

