import unittest
from src.password_check import mask_password

class TestMaskPassword(unittest.TestCase):

    def test_short_password_all_hidden(self):
        self.assertEqual(mask_password("abc"), "***")
        self.assertEqual(mask_password("1234"), "****")

    def test_medium_password_masked(self):
        self.assertEqual(mask_password("abcde"), "a***e")
        self.assertEqual(mask_password("hello"), "h***o")

    def test_long_password_masked(self):
        self.assertEqual(mask_password("password123"), "p*********3")

    def test_empty_password(self):
        self.assertEqual(mask_password(""), "")

if __name__ == "__main__":
    unittest.main()