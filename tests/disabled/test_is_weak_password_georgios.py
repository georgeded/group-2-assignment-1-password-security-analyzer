import unittest
from src.password_check import is_weak_password

class TestIsWeakPassword(unittest.TestCase):
    def test_empty_password(self):
        self.assertTrue(is_weak_password(""))

    def test_short_password(self):
        self.assertTrue(is_weak_password("Ab1@"))

    def test_no_uppercase(self):
        self.assertTrue(is_weak_password("ab1@1234"))

    def test_no_lowercase(self):
        self.assertTrue(is_weak_password("AB1@1234"))

    def test_no_digit(self):
        self.assertTrue(is_weak_password("Abc@defg"))

    def test_no_special_character(self):
        self.assertTrue(is_weak_password("Abc12345"))

    def test_valid_strong_password(self):
        self.assertFalse(is_weak_password("Abc@1234"))

if __name__ == "__main__":
    unittest.main()