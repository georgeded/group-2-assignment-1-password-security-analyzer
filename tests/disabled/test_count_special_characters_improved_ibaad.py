import unittest
from src.password_check import count_special_characters

class TestCountSpecialCharactersImproved(unittest.TestCase):
    def test_no_special_chars(self):
        self.assertEqual(count_special_characters("abc123"), 0)

    def test_empty_password(self):
        self.assertEqual(count_special_characters(""), 0)

    def test_digits_only(self):
        self.assertEqual(count_special_characters("1234567890"), 0)

    def test_alpha_only(self):
        self.assertEqual(count_special_characters("abcdef"), 0)

    def test_contains_space(self):
        self.assertEqual(count_special_characters("abc !@#"), -1)
        self.assertEqual(count_special_characters("   "), -1)

    def test_too_short_length(self):
        self.assertEqual(count_special_characters("!@#"), -2)
        self.assertEqual(count_special_characters("ab#"), -2)

    def test_mixed_specials(self):
        self.assertEqual(count_special_characters("abc!@#123"), 3)
        self.assertEqual(count_special_characters("hello.world?"), 2) 

    def test_all_special_chars(self):
        specials = "!@#$%^&*"
        self.assertEqual(count_special_characters(specials), len(specials))

    def test_numbers_and_specials(self):
        self.assertEqual(count_special_characters("1234!%"), 2)
        self.assertEqual(count_special_characters("9*8(7)"), 3) 

if __name__ == "__main__":
    unittest.main()
