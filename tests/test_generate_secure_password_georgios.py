import unittest
from src.password_check import generate_secure_password, is_strong_password

class TestGenerateSecurePassword(unittest.TestCase):
    def test_default_length(self):
        password = generate_secure_password()
        self.assertTrue(is_strong_password(password))
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        password = generate_secure_password(16)
        self.assertTrue(is_strong_password(password))
        self.assertEqual(len(password), 16)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_secure_password(6)

    def test_minimum_valid_length(self):
        password = generate_secure_password(8)
        self.assertTrue(is_strong_password(password))
        self.assertEqual(len(password), 8)

    def test_maximum_valid_length(self):
        password = generate_secure_password(64)
        self.assertTrue(is_strong_password(password))
        self.assertEqual(len(password), 64)

if __name__ == "__main__":
    unittest.main()