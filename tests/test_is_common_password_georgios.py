import unittest
from src.password_check import is_common_password

class TestIsCommonPassword(unittest.TestCase):
    def test_common_password(self):
        self.assertTrue(is_common_password("123456"))
        self.assertTrue(is_common_password("password"))
        self.assertTrue(is_common_password("qwerty"))
        self.assertTrue(is_common_password("abc123"))
        self.assertTrue(is_common_password("123456789"))
        self.assertTrue(is_common_password("password123"))

    def test_not_common_password(self):
        self.assertFalse(is_common_password("uniquePassword123!"))
        self.assertFalse(is_common_password("secure@password"))
        self.assertFalse(is_common_password("randomString"))
        self.assertFalse(is_common_password("notInList"))

    def test_edge_cases(self):
        self.assertFalse(is_common_password(""))
        self.assertFalse(is_common_password(" "))

if __name__ == "__main__":
    unittest.main()