import unittest
from src.password_check import suggest_password_improvements

class TestSuggestPasswordImprovements(unittest.TestCase):
    def test_suggest_password_improvements(self):
        self.assertEqual(suggest_password_improvements(""), [
            "Password cannot be empty.",
            "Increase the password length to at least 8 characters.",
            "Add at least one uppercase letter.",
            "Add at least one lowercase letter.",
            "Include at least one digit.",
            "Include at least one special character."
        ])

        self.assertEqual(suggest_password_improvements("short"), [
            "Increase the password length to at least 8 characters.",
            "Add at least one uppercase letter.",
            "Include at least one digit.",
            "Include at least one special character.",
            "Avoid sequential characters like 'abcd' or '1234'."
        ])

        self.assertEqual(suggest_password_improvements("NoDigitsPassword!"), [
            "Include at least one digit.",
            "Avoid sequential characters like 'abcd' or '1234'."
        ])

        self.assertEqual(suggest_password_improvements("NoSpecialCharsPassword123"), [
            "Include at least one special character.",
            "Avoid sequential characters like 'abcd' or '1234'."
        ])
        
        self.assertEqual(suggest_password_improvements("Password123!"), [
            "Avoid sequential characters like 'abcd' or '1234'.",
            "Avoid using common passwords."
        ])

        self.assertEqual(suggest_password_improvements("Pass Word@!1"), [
            "Avoid sequential characters like 'abcd' or '1234'.",
            "Avoid spaces in your password."
        ])

        self.assertEqual(suggest_password_improvements("tr0ng#Pw4@"), [
            "Your password is strong!"
        ])

        self.assertEqual(suggest_password_improvements("aaaaaa1!@B"), [
            "Avoid sequential characters like 'abcd' or '1234'.",
            "Avoid repeated characters."
        ])
