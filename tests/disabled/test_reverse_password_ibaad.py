import unittest
from src.password_check import reverse_password

class TestReversePassword(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse_password(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_password("a"), "a")

    def test_reverse(self):
        self.assertEqual(reverse_password("abc"), "cba")
        self.assertEqual(reverse_password("hello"), "olleh")

    def test_palindrome(self):
        self.assertEqual(reverse_password("madam"), "madam")
        self.assertEqual(reverse_password("racecar"), "racecar")

    def test_special_characters(self):
        self.assertEqual(reverse_password("!@#$"), "$#@!")
        self.assertEqual(reverse_password("a!b@c"), "c@b!a")

    def test_numeric_string(self):
        self.assertEqual(reverse_password("12345"), "54321")

    def test_mixed_string(self):
        self.assertEqual(reverse_password("Abc123!"), "!321cbA")

    def test_whitespace(self):
        self.assertEqual(reverse_password(" "), " ")
        self.assertEqual(reverse_password("a b c"), "c b a")
        self.assertEqual(reverse_password("  abc  "), "  cba  ")

if __name__ == "__main__":
    unittest.main()