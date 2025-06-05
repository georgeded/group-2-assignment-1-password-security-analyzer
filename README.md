# Report for Assignment 1

## Project

Description: The **Password Security Analyzer** is a tool designed to evaluate the strength and security of passwords. It provides features such as checking password strength, detecting common weaknesses (sequential or repeated characters), generating secure and memorable passwords, calculating password entropy (uniqueness), and offering suggestions for improvement. The tool also includes a CLI for user interaction.

Programming language: Python

## Initial tests

### Tests
#### Initial Test 1 (George)

```python
import unittest
from src.password_check import is_strong_password

class TestStrongPassword(unittest.TestCase):
    def test_is_strong_password_ShortPassword_False(self):
        pw = "Ab1@"
        res = is_strong_password(pw)
        self.assertFalse(res, "Password shorter than 8 characters should not be strong.")

if __name__ == '__main__':
    unittest.main()
```

#### Description
This test validates the is_strong_password function by checking if it correctly identifies passwords shorter than 8 characters as not strong. The password "Ab1@" is used as input, and the expected result is False.

#### Initial Test 2 (Dean)
```python
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
```
#### Description
My test validates suggest_password_improvements() function by checking if a strong password is identified correctly, and if a password which needs improvements is correctly identified.

### Coverage of initial tests

TODO: Inform the name of the existing tool that was executed and how it was executed

TODO: Show the coverage results provided by the existing tool with a screenshot

## Coverage improvement

### Individual tests

TODO: The following is supposed to be repeated for each group member

TODO: Group member name

TODO: Test 1

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

TODO: Provide a screenshot of the new coverage results

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

Repeat for other tests...

### Overall

TODO: Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)

TODO: Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group

## Statement of individual contributions

TODO: Write what each group member did. Use the following table for that and add additional text under it if you see fit.

| Member | Three functions (names with links to the code on the repository) created | Initial test (name) | Other tests (names) |
| --- | --- | --- | --- |
| Georgios Dedempilis  | [is_strong_password](src/password_check.py#L6), [is_weak_password](src/password_check.py#L14), [has_sequential_chars](src/password_check.py#L18), [has_spaces](src/password_check.py#L77), [reverse_password](src/password_check.py#L81) | TestStrongPassword (Initial Test 1) |                     |
| Dean Kok | [suggest_password_improvements](src/password_check.py#L115), [is_common_password](src/password_check.py#30), [has_repeated_chars](src/password_check.py#111)| test_suggest_improvement.py (Initial Test 2) | |
| Member C | | | |
| Member D | | | |
