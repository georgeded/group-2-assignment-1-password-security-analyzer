import unittest
from src.password_check import reverse_password

class TestReversePassword(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse_password(""), "")

    def test_short(self):
        self.assertEqual(reverse_password("a"), "a")
        self.assertEqual(reverse_password("ab"), "ab")

    def test_reverse(self):
        self.assertEqual(reverse_password("abc"), "cba")
        self.assertEqual(reverse_password("hello"), "olleh")

    def test_palindrome(self):
        self.assertEqual(reverse_password("madam"), "madam")

if __name__ == "__main__":
    unittest.main()
