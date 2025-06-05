import unittest
from src.password_check import suggest_password_improvements

class TestSuggestPasswordImprovements(unittest.TestCase):
    def test_suggest_password_improvements(self):
        self.assertEqual(suggest_password_improvements("password123"), [
            "Add at least one uppercase letter.",
            "Include at least one special character.",
            "Avoid sequential characters like 'abcd' or '1234'.",
            "Avoid using common passwords."
        ])
        
        self.assertEqual(suggest_password_improvements("P@ssw0rd!"), [
            "Your password is strong!"
        ])

if __name__ == "__main__":
    unittest.main()