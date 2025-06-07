import unittest
from src.password_check import mask_password

class TestMaskPasswordImproved(unittest.TestCase):
    def test_empty_password(self):
        self.assertEqual(mask_password(""), "")

    def test_very_short_password(self):
        self.assertEqual(mask_password("a"), "*")

    def test_exactly_two_characters(self):
        self.assertEqual(mask_password("ab"), "**")

    def test_exactly_three_characters(self):
        self.assertEqual(mask_password("abc"), "a*c")

    def test_exactly_four_characters(self):
        self.assertEqual(mask_password("1234"), "1**4")

    def test_long_password(self):
        self.assertEqual(mask_password("password123456"), "p************6")

    def test_special_characters(self):
        self.assertEqual(mask_password("@bc!"), "@**!")

    def test_numeric_password(self):
        self.assertEqual(mask_password("123456"), "1****6")

    def test_alphabetic_password(self):
        self.assertEqual(mask_password("abcdef"), "a****f")