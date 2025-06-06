import unittest
from src.password_check import mask_password

class TestMaskPassword(unittest.TestCase):
    def test_long_password_masked(self):
        self.assertEqual(mask_password("password123"), "p*********3")
    def test_numeric_password_masked(self):
        self.assertEqual(mask_password("123"), "1*3")

if __name__ == "__main__":
    unittest.main()