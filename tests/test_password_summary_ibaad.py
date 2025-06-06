import unittest
from src.password_check import password_summary

class TestPasswordSummary(unittest.TestCase):
    def test_numeric_sequence(self):
        summary = password_summary("1234")
        self.assertFalse(summary["is_strong"])
        self.assertTrue(summary["is_weak"])
        self.assertTrue(summary["has_sequential_chars"])
        self.assertFalse(summary["is_common"])
        self.assertEqual(summary["special_char_count"], 0)
        self.assertFalse(summary["has_spaces"])
        self.assertEqual(summary["reversed"], "4321")
        self.assertEqual(summary["masked"], "*234*")

    def test_typical_strong(self):
        pw = "Ab1@xyz"
        summary = password_summary(pw)
        self.assertTrue(summary["is_strong"])
        self.assertFalse(summary["is_weak"])
        self.assertTrue(summary["has_sequential_chars"])
        self.assertFalse(summary["is_common"])
        self.assertGreater(summary["entropy"], 0)
        self.assertEqual(summary["character_types"]["uppercase"], 1)
        self.assertEqual(summary["character_types"]["lowercase"], 4)
        self.assertEqual(summary["character_types"]["digits"], 1)
        self.assertEqual(summary["character_types"]["special"], 1)
        self.assertEqual(summary["special_char_count"], 1)
        self.assertFalse(summary["has_spaces"])
        self.assertEqual(summary["reversed"], "zyx@1bA")
        self.assertEqual(summary["masked"], "A*****z")

    def test_with_space_and_common(self):
        summary = password_summary("password 1")
        self.assertFalse(summary["is_strong"])
        self.assertTrue(summary["is_weak"])
        self.assertTrue(summary["has_spaces"])
        self.assertFalse(summary["is_common"])
        self.assertEqual(summary["masked"], "p*******1")

if __name__ == "__main__":
    unittest.main()
