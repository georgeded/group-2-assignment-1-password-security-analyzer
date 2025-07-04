# Report for Assignment 1

## Project

Description: The **Password Security Analyzer** is a tool designed to evaluate the strength and security of passwords. It provides features such as checking password strength, detecting common weaknesses (sequential or repeated characters), generating secure and memorable passwords, calculating password entropy (uniqueness), and offering suggestions for improvement. The tool also includes a CLI for user interaction.

Programming language: Python

## Initial tests

### Tests
#### Initial Test 1 (Georgios)

```python
import unittest
from src.password_check import is_strong_password

#Test that a password shorter than 8 characters is not strong.

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
        

if __name__ == "__main__":
    unittest.main()
```
#### Description
My test validates suggest_password_improvements() function by checking if a password which needs improvements is correctly identified.

#### Initial Test 3 (Emincan)
```python
import unittest
from src.password_check import mask_password

class TestMaskPassword(unittest.TestCase):
    def test_long_password_masked(self):
        self.assertEqual(mask_password("password123"), "p*********3")
    def test_numeric_password_masked(self):
        self.assertEqual(mask_password("123"), "1*3")

if __name__ == "__main__":
    unittest.main()
```
#### Description
My test validates the mask_password() function by checking if passwords show only the first and last character while masking the rest. This is verified through 2 test cases, including medium and small passwords.

#### Initial Test 4 (Ibaad)
```python
import unittest
from src.password_check import count_special_characters

class TestCountSpecialCharacters(unittest.TestCase):

    def test_no_special_chars(self):
        self.assertEqual(count_special_characters("abc123"), 0)

    def test_empty_password(self):
        self.assertEqual(count_special_characters(""), 0)

if __name__ == "__main__":
    unittest.main()
```
#### Description
This test verifies that the count_special_characters function correctly returns the number of special characters in various passwords (no special, and empty).

### Coverage of initial tests

**Tool Name:** Coverage.py

**Execution Steps:**
1. Install Coverage.py:
   ```bash
   pip install coverage
   ```
   Run tests with coverage:
   ```bash 
   coverage run -m unittest discover tests
    ```
   Generate coverage report:
   ```bash
   coverage report
   ```

**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage Result](reports/final_coverability.png)

## Coverage improvement

### Individual tests

-----------Test cases of Emincan Yildiz-----------

**Group Member:** Emincan Yildiz

**Test 1:** test_mask_password_improved_emincan.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/9fede675a589494a2be3537962baee75aaa64771)

**Screenshot: Old Coverage Result (Before Improvement)**
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**
This improved test significantly expands the coverage for the mask_password() function. While the initial test only checked medium and small passwords, this improved version includes edge cases such as:
- Empty string
- Very short passwords (length 1–2)
- Exactly 4 characters
- Longer passwords
- Passwords with digits and passwords with special characters
These test cases activate all logical branches in the function and ensure correct behavior for different string lengths.

**Coverage improvement:** 89% → 100%

---------------------------

**Group Member:** Emincan Yildiz

**Test 2:** test_character_type_count_emincan.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/dce97b74e3f1c7400e18d68f672e2467a2c2c72c).

**Screenshot: Old Coverage Result (Before Improvement)**
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**
There were no previous tests for the character_type_count() function, so its initial coverage was 0%.
This test improves coverage by thoroughly checking all character type branches:
- Only uppercase characters
- Only lowercase characters
- Only digits
- Only special characters
- Mixed characters (at least one of each type)
- Edge case with an empty string
Each condition in the function is now triggered by specific inputs, ensuring that all logical paths are tested.

**Coverage improvement:** 0% → 100%

---------------------------

**Group Member:** Emincan Yildiz

**Test 3:** test_has_sequential_chars_emincan.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/a65698b3c15c160dcbd93f996b372419b971a636).

**Screenshot: Old Coverage Result (Before Improvement)**
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**
There were no previous tests for the has_sequential_chars() function, so its initial coverage was 0%.
This improved test ensures all key logical paths are exercised by including inputs with:
- Alphabetic sequences ("abcd", "lmno")
- Numeric sequences ("1234", "a1234z")
- Sequences in the middle of the string ("xxabcdxx")
- Custom sequence lengths ("abc" with seq_len=3)
- Strings shorter than the sequence length ("ab")
- Strings without any sequence ("a1b2c3")
All conditions and loop paths in the function are exercised through the test cases, providing maximum practical coverage based on the function’s logic.

**Coverage improvement:** 0% → 100%

-----------Test cases of Georgios Dedempilis-----------

**Group Member:** Georgios Dedempilis

**Test 1:** test_is_weak_password_georgios.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/f43c7bfe0727c1055156d54966b6391f68bc52a3)

**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**  
This test thoroughly evaluates the `is_weak_password()` function by addressing all possible edge cases. It ensures the function correctly identifies weak passwords, including:
- Empty passwords
- Short passwords that fail the length requirement
- Passwords missing essential components like uppercase letters, lowercase letters, digits, or special characters
- Passwords containing spaces
- Strong passwords that should not be classified as weak

By covering all logical branches, this test ensures the function behaves as expected for various password scenarios. There were no previous tests for this function, so its initial coverage was 0%.


**Coverage improvement:** 0% → 100%

---------------------------

**Test 2:** test_strong_password_improved_georgios.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/f43c7bfe0727c1055156d54966b6391f68bc52a3)

**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**  
This test enhances the coverage for the `is_strong_password()` function by introducing edge cases that were previously untested. It ensures the function correctly identifies strong passwords and rejects weak ones, including:
- Short passwords that fail the minimum length requirement
- Passwords missing one or more essential components (uppercase, lowercase, digits, special characters)
- Numeric-only passwords that lack complexity
- Passwords with spaces that reduce security
- Valid strong passwords that meet all criteria

The test ensures all logical branches are exercised, validating the function's robustness.


**Coverage improvement:** 89% → 100%

---------------------------

**Test 3:** test_is_common_password_georgios.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/f43c7bfe0727c1055156d54966b6391f68bc52a3)

**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**  
This test ensures comprehensive coverage for the `is_common_password()` function by testing various scenarios. It validates the function's ability to:
- Identify passwords from the predefined list of common passwords
- Reject passwords that are not in the list
- Handle edge cases like empty strings and single spaces

By testing all logical branches, this test guarantees the function accurately differenctiation between common and uncommon passwords. There were no previous tests for this function, so its initial coverage was 0%.

**Coverage improvement:** 0% → 100%

---------------------------

**Test 4:** test_generate_secure_password_georgios.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/f43c7bfe0727c1055156d54966b6391f68bc52a3)

**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**  
This test expands the coverage for the `generate_secure_password()` function by addressing edge cases and validating its behavior for different inputs. It ensures the function:
- Generates passwords of default length
- Handles custom lengths correctly
- Rejects invalid lengths (too short or negative values)
- Successfully generates passwords at the minimum and maximum valid lengths

By testing all logical branches, this test ensures the function reliably produces secure passwords under various conditions. There were no previous tests for this function, so its initial coverage was 0%.

**Coverage improvement:** 0% → 100%

---------------------------

**Test 5:** test_password_entropy_georgios.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/f43c7bfe0727c1055156d54966b6391f68bc52a3)

**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**  
This test ensures the `password_entropy()` function is thoroughly evaluated by testing a wide range of inputs. It validates the function's ability to calculate entropy for:
- Empty passwords
- Single-character passwords
- Passwords with repeated characters
- Passwords containing only uppercase, lowercase, digits, or special characters
- Mixed passwords with a combination of all character types

By covering all logical branches, this test guarantees the function accurately calculates entropy for diverse password scenarios. There were no previous tests for this function, so its initial coverage was 0%.

**Coverage improvement:** 0% → 100%

-----------Test cases of Dean Kok-----------
**Group Member:** Dean Kok

**Test 1:** test_suggest_improvement.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/17a67aff66a3ad71bbece2c6132dcea834a46cc6)

**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**  
This test thoroughly evaluates the `suggest_password_improvements()` function by addressing all possible edge cases. It ensures the function correctly identifies passwords which can be improved, based on the absence of certain key characteristics of strong passwords. It checks the following:
- Short (<8 characters) passwords
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character
- No sequential characters in the password
- No repeated characters in the password
- Not a common password (predefined list)
- No spaces in the password

**Coverage improvement:** 86% → 100%

---------------------------

**Group Member:** Dean Kok

**Test 2:** test_is_palindrome_password.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/f34c410dbb8743bfd141ff56e27b824d9b0bd5af)

**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**  
This test evaluates whether the is_palindrome_password() function works correctly.

**Coverage improvement:** 0% → 100%

---------------------------

**Group Member:** Dean Kok

**Test 3:** test_generate_memorable_password.py

**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/203b91e077484c7b86f1c63e5820ea42a6681b89)

**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage Result](reports/final_coverability.png)

**Coverage Improvement Explanation:**  
This test evaluates whether the generate_memorable_password() function works correctly. It checks if there correctly get generated capitalized words, ending in a special character and then a digit.

**Coverage improvement:** 0% → 100%

-----------Test cases of Ibaad Rahman-----------

**Group Member:** Ibaad Rahman  

**Test 1:** `improved_test_count_special_characters.py`  
**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/7496aa5e3b68f4a944ca20ce35a1a52377347ba5)  
**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage](reports/initial%20coverability%20analysis%20.png)  
**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage](reports/final_coverability.png)  
**Coverage Improvement Explanation:**  
This improved test exercises every branch in `count_special_characters()` by covering:  
- letters + digits only (returns 0)  
- empty string (returns 0)  
- digits‐only (returns 0)  
- alpha‐only (returns 0)  
- any space present (returns –1)  
- length < 5 (returns –2)  
- mixed letters, digits, punctuation (counts punctuation)  
- all punctuation (counts all chars)  
- digits + specials mixed (counts only punctuation)  

**Coverage improvement:** 89% → 100%

---

**Test 2:** `test_reverse_password_ibaad.py`  
**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/df2fceae88d9fdedeb7302ac48504714ed8ea923)  
**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage](reports/initial%20coverability%20analysis%20.png)  
**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage](reports/final_coverability.png)  
**Coverage Improvement Explanation:**  
Adding this test now covers all cases in `reverse_password()` by exercising:  
- empty string → `""`  
- length 1–2 → returns original  
- standard reversal for length ≥ 3  
- palindrome (reverses to itself)  

**Coverage improvement:** 0% → 100%

---

**Test 3:** `test_password_summary_ibaad.py`  
**Patch/Commit:** [View Commit](https://github.com/georgeded/group-2-assignment-1-password-security-analyzer/commit/7e1e80649abd30798211514cb9e8a43856b9d2fa)  
**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage](reports/initial%20coverability%20analysis%20.png)  
**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage](reports/final_coverability.png)  
**Coverage Improvement Explanation:**  
This test drives every branch in `password_summary()` by including:  
- numeric sequence (`"1234"`) → triggers `has_sequential_chars`  
- typical strong password (`"Ab1@xyz"`) → triggers strong‐password path, non‐common, non‐space, correct entropy, character counts, reversal and masking  
- space‐containing input (`"password 1"`) → triggers weak, `has_spaces`, and masking logic  

**Coverage improvement:** 0% → 100%

### Overall

**Screenshot: Old Coverage Result (Before Improvement)**  
![Old Coverage Result](reports/initial%20coverability%20analysis%20.png)

**Screenshot: New Coverage Result (After Improvement)**  
![New Coverage Result](reports/final_coverability.png)

## Statement of individual contributions

| Member             | Three functions (names with links to the code on the repository) created                                                                 | Initial test (name)                     | Other tests (names)                                                                                     |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------|
| Georgios Dedempilis | [is_strong_password](src/password_check.py#L6), [is_weak_password](src/password_check.py#L22), [has_sequential_chars](src/password_check.py#L41), [has_spaces](src/password_check.py#L111), [password_entropy](src/password_check.py#L63) | initial_test_strong_password.py         | test_strong_password_improved_georgios.py, test_is_common_password_georgios.py, test_generate_secure_password_georgios.py, test_password_entropy_georgios.py |
| Dean Kok           | [suggest_password_improvements](src/password_check.py#L196), [is_common_password](src/password_check.py#L57), [has_repeated_chars](src/password_check.py#L183) | initial_test_suggest_improvement.py     | [test_suggest_improvement.py](tests/test_suggest_improvement.py)     , [test_generate_memorable_password.py](tests/test_generate_memorable_password.py), [test_is_palindrome_password](tests/test_is_palindrome_password.py)                                                                                                    |
| Emincan Yildiz     | [main](src/password_check.py#L212), [generate_memorable_password](src/password_check.py#L196), [mask_password](src/password_check.py#L133) | initial_test_mask_password.py           | test_mask_password_improved_emincan.py, test_character_type_count_emincan.py, test_has_sequential_chars_emincan.py |
| Ibaad Rahman       | [count_special_characters](src/password_check.py#L89), [reverse_password](src/password_check.py#L96), [character_type_count](src/password_check.py#L81), [password_summary](src/password_check.py#L150) | initial_test_count_special_characters.py |  improved_test_count_special_characters.py, test_reverse_password_ibaad.py, test_password_summary_ibaad.py                                                                                                       |
