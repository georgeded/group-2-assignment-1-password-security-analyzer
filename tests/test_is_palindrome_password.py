import unittest
from src.password_check import is_palindrome_password

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_password(self):
        self.assertTrue(is_palindrome_password("abccba"))
    
    def test_non_palindrome_password(self):
        self.assertFalse(is_palindrome_password("abcde"))
    
    def test_empty_password(self):
        self.assertFalse(is_palindrome_password(""))