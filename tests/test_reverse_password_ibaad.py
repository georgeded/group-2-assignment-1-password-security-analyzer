import unittest
from src.password_check import reverse_password

class TestReversePassword(unittest.TestCase):
    def test_empty_string(self):
        # If password is empty, function should return ""
        self.assertEqual(reverse_password(""), "")

    def test_short_strings(self):
        # If password length < 3, function returns the same string
        self.assertEqual(reverse_password("a"), "a")
        self.assertEqual(reverse_password("ab"), "ab")

    def test_regular_string(self):
        # For length >= 3, it should simply reverse
        self.assertEqual(reverse_password("abc"), "cba")
        self.assertEqual(reverse_password("hello"), "olleh")

    def test_palindrome(self):
        # A palindrome should reverse to the same palindrome
        self.assertEqual(reverse_password("madam"), "madam")

if __name__ == "__main__":
    unittest.main()
