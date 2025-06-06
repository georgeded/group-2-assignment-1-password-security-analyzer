import unittest
import string
from src.password_check import character_type_count

class TestCharacterTypeCount(unittest.TestCase):

    def test_only_uppercase(self):
        result = character_type_count("ABCDEF")
        self.assertEqual(result["uppercase"], 6)
        self.assertEqual(result["lowercase"], 0)
        self.assertEqual(result["digits"], 0)
        self.assertEqual(result["special"], 0)

    def test_only_lowercase(self):
        result = character_type_count("abcdef")
        self.assertEqual(result["uppercase"], 0)
        self.assertEqual(result["lowercase"], 6)
        self.assertEqual(result["digits"], 0)
        self.assertEqual(result["special"], 0)

    def test_only_digits(self):
        result = character_type_count("123456")
        self.assertEqual(result["uppercase"], 0)
        self.assertEqual(result["lowercase"], 0)
        self.assertEqual(result["digits"], 6)
        self.assertEqual(result["special"], 0)

    def test_only_special_characters(self):
        result = character_type_count("!?@#%&")
        self.assertEqual(result["uppercase"], 0)
        self.assertEqual(result["lowercase"], 0)
        self.assertEqual(result["digits"], 0)
        self.assertEqual(result["special"], 6)

    def test_mixed_characters(self):
        result = character_type_count("Aa1!")
        self.assertEqual(result["uppercase"], 1)
        self.assertEqual(result["lowercase"], 1)
        self.assertEqual(result["digits"], 1)
        self.assertEqual(result["special"], 1)

    def test_empty_password(self):
        result = character_type_count("")
        self.assertEqual(result["uppercase"], 0)
        self.assertEqual(result["lowercase"], 0)
        self.assertEqual(result["digits"], 0)
        self.assertEqual(result["special"], 0)

if __name__ == "__main__":
    unittest.main()