import unittest
from src.password_check import is_strong_password

class TestStrongPasswordImproved(unittest.TestCase):
    def test_short_password(self):
        self.assertFalse(is_strong_password("Ab1@"))

    def test_no_uppercase(self):
        self.assertFalse(is_strong_password("ab1@1234"))

    def test_no_lowercase(self):
        self.assertFalse(is_strong_password("AB1@1234"))

    def test_no_digit(self):
        self.assertFalse(is_strong_password("Abc@defg"))

    def test_no_special_character(self):
        self.assertFalse(is_strong_password("Abc12345"))

    def test_contains_spaces(self):
        self.assertFalse(is_strong_password("Abc 123@"))

    def test_numeric_only(self):
        self.assertFalse(is_strong_password("12345678"))

    def test_valid_strong_password(self):
        self.assertTrue(is_strong_password("Abc@1234"))

if __name__ == "__main__":
    unittest.main()