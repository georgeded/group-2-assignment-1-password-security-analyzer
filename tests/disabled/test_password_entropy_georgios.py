import unittest
from src.password_check import password_entropy

class TestPasswordEntropy(unittest.TestCase):
    def test_empty_password(self):
        self.assertEqual(password_entropy(""), 0)

    def test_lowercase_only(self):
        self.assertAlmostEqual(password_entropy("abcdef"), 28.2, places=1)

    def test_uppercase_only(self):
        self.assertAlmostEqual(password_entropy("ABCDEF"), 28.2, places=1)

    def test_digits_only(self):
        self.assertAlmostEqual(password_entropy("123456"), 19.9, places=1)

    def test_special_characters_only(self):
        self.assertAlmostEqual(password_entropy("!@#$%^"), 30.0, places=1)

    def test_mixed_characters(self):
        self.assertAlmostEqual(password_entropy("Abc123!"), 45.882, places=1)

    def test_no_entropy(self):
        self.assertEqual(password_entropy(""), 0)

    def test_single_character(self):
        self.assertAlmostEqual(password_entropy("a"), 4.7, places=1)

    def test_repeated_characters(self):
        self.assertAlmostEqual(password_entropy("aaa"), 14.1, places=1)

if __name__ == "__main__":
    unittest.main()