import unittest
from src.password_check import mask_password

class TestMaskPasswordImproved(unittest.TestCase):

    def test_empty_password(self):
        self.assertEqual(mask_password(""), "")

    def test_very_short_password(self):
        self.assertEqual(mask_password("a"), "*")
        self.assertEqual(mask_password("ab"), "**")

    def test_exactly_four_characters(self):
        self.assertEqual(mask_password("1234"), "****")
        self.assertEqual(mask_password("test"), "****")

    def test_exactly_five_characters(self):
        self.assertEqual(mask_password("hello"), "h***o")

    def test_long_password(self):
        self.assertEqual(mask_password("password123"), "p*********3")

    def test_special_characters(self):
        self.assertEqual(mask_password("@bc!"), "@**!")

    def test_numeric_password(self):
        self.assertEqual(mask_password("98765"), "9***5")

if __name__ == "__main__":
    unittest.main()