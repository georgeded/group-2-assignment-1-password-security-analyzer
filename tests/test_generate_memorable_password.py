import unittest
import re
from src.password_check import generate_memorable_password

class TestGenerateMemorablePassword(unittest.TestCase):
    def test_default_word_count(self):
        password = generate_memorable_password()
        # verifies 4 capitalized words, one special character, and one digit
        self.assertTrue(re.match(r'^([A-Z][a-z]+){4}[^a-zA-Z0-9][0-9]$', password))

    def test_custom_word_count(self):
        password = generate_memorable_password(words=6)
        # verifies 6 capitalized words plus a special char and digit
        self.assertTrue(re.match(r'^([A-Z][a-z]+){6}[^a-zA-Z0-9][0-9]$', password))

    def test_minimum_word_count(self):
        password = generate_memorable_password(words=1)
        self.assertEqual(password, "Too few words to generate a password.")

    def test_maximum_word_count(self):
        password = generate_memorable_password(words=11)
        self.assertEqual(password, "Too many words to generate a password.")
        
    def test_boundary_values(self):
        # test boundaries
        min_password = generate_memorable_password(words=2)
        self.assertTrue(re.match(r'^([A-Z][a-z]+){2}[^a-zA-Z0-9][0-9]$', min_password))
        
        max_password = generate_memorable_password(words=10)
        self.assertTrue(re.match(r'^([A-Z][a-z]+){10}[^a-zA-Z0-9][0-9]$', max_password))