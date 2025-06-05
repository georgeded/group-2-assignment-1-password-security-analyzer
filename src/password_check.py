import random
import string
import math

# checks if the password is strong (length at least 8, cupper/lowercase, digits, special characters).
def is_strong_password(pw):
    if len(pw) < 8:
        return False
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(c in string.punctuation for c in pw)
    return has_upper and has_lower and has_digit and has_special

# check if the password weak
def is_weak_password(pw):
    return not is_strong_password(pw)

# sequential characters like abcd or 1234
def has_sequential_chars(pw, seq_len=4):
    for i in range(len(pw) - seq_len + 1):
        segment = pw[i:i + seq_len]
        if segment.isalpha() and segment == ''.join(sorted(segment)):
            return True
        if segment.isdigit() and segment == ''.join(sorted(segment)):
            return True
    return False

# password is in of common passwords
def is_common_password(pw):
    common_passwords = [
        "123456", "password", "123456789", "qwerty",
        "abc123", "letmein", "welcome", "admin", "12345678",
        "password1", "1234567", "iloveyou", "12345",
        "1234567890", "123123", "qwertyuiop", "monkey",
        "1234", "sunshine", "123321", "trustno1",
        "dragon", "baseball", "football", "123456a", "1q2w3e4r"
        "123456789a", "qwerty123", "1qaz2wsx", "qazwsx",
        "1q2w3e", "qwerty1", "123qwe", "password123"
    ]
    return pw in common_passwords

# generates a secure password that passes all checks
def generate_secure_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    while True:
        pw = ''.join(random.choices(
            string.ascii_letters + string.digits + string.punctuation,
            k=length
        ))
        if is_strong_password(pw):
            return pw

# entropy of password in bits: measure of how unpredictable or secure a password is
def password_entropy(pw):
    char_set_size = 0
    if any(c.islower() for c in pw):
        char_set_size += 26
    if any(c.isupper() for c in pw):
        char_set_size += 26
    if any(c.isdigit() for c in pw):
        char_set_size += 10
    if any(c in string.punctuation for c in pw):
        char_set_size += len(string.punctuation)
    return 0 if char_set_size == 0 else len(pw) * math.log2(char_set_size)

# number of character types
def character_type_count(pw):
    return {
        "uppercase": sum(1 for c in pw if c.isupper()),
        "lowercase": sum(1 for c in pw if c.islower()),
        "digits": sum(1 for c in pw if c.isdigit()),
        "special": sum(1 for c in pw if c in string.punctuation)
    }

# count the number of special characters.
def count_special_characters(pw):
    return sum(1 for c in pw if c in string.punctuation)

# checks if contains spaces.
def has_spaces(pw):
    return " " in pw

# reverses the password.
def reverse_password(pw):
    return pw[::-1]

# hide the middle characters of the password.
def mask_password(pw):
    if len(pw) <= 4:
        return "*" * len(pw)
    return pw[0] + "*" * (len(pw) - 2) + pw[-1]

# summarizing the password properties.
def password_summary(pw):
    return {
        "is_strong": is_strong_password(pw),
        "is_weak": is_weak_password(pw),
        "has_sequential_chars": has_sequential_chars(pw),
        "is_common": is_common_password(pw),
        "entropy": password_entropy(pw),
        "character_types": character_type_count(pw),
        "special_char_count": count_special_characters(pw),
        "has_spaces": has_spaces(pw),
        "reversed": reverse_password(pw),
        "masked": mask_password(pw),
    }

# check if contains more than 3 repeated characters 
def has_repeated_chars(pw, threshold=3):
    return any(pw.count(char) > threshold for char in set(pw))

# suggests improvements for strong password.
def suggest_password_improvements(pw):
    suggestions = []

    if len(pw) < 8:
        suggestions.append("Increase the password length to at least 8 characters.")
    if not any(c.isupper() for c in pw):
        suggestions.append("Add at least one uppercase letter.")
    if not any(c.islower() for c in pw):
        suggestions.append("Add at least one lowercase letter.")
    if not any(c.isdigit() for c in pw):
        suggestions.append("Include at least one digit.")
    if not any(c in string.punctuation for c in pw):
        suggestions.append("Include at least one special character.")
    if has_sequential_chars(pw):
        suggestions.append("Avoid sequential characters like 'abcd' or '1234'.")
    if has_repeated_chars(pw):
        suggestions.append("Avoid repeated characters.")
    if is_common_password(pw):
        suggestions.append("Avoid using common passwords.")

    return suggestions if suggestions else ["Your password is strong!"]

# memorable password using random words and special characters.
def generate_memorable_password(words=4):
    word_list = [
        "apple", "banana", "cherry", "dragon", "elephant",
        "falcon", "grape", "honey", "island", "jungle"
    ]
    password = ''.join(random.choice(word_list).capitalize() for _ in range(words))
    special_char = random.choice(string.punctuation)
    digit = random.choice(string.digits)
    return f"{password}{special_char}{digit}"

# check if is a palindrome (anna)
def is_palindrome_password(pw):
    return pw == pw[::-1]

def main():
    print("Welcome to the Password Security Analyzer!")
    print("Choose an option:")
    print("1. Check if a password is strong")
    print("2. Get a password summary")
    print("3. Suggest password improvements")
    print("4. Generate a secure password")
    print("5. Generate a memorable password")
    print("6. Check if a password is a palindrome")
    print("7. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice (1-7): "))
            if choice == 1:
                pw = input("Enter the password to check: ")
                print("Strong password:", is_strong_password(pw))
            elif choice == 2:
                pw = input("Enter the password to summarize: ")
                summary = password_summary(pw)
                print("Password Summary:")
                for key, value in summary.items():
                    print(f"  {key}: {value}")
            elif choice == 3:
                pw = input("Enter the password to improve: ")
                suggestions = suggest_password_improvements(pw)
                print("Suggestions to improve your password:")
                for suggestion in suggestions:
                    print(f"  - {suggestion}")
            elif choice == 4:
                length = int(input("Enter the desired password length (minimum 8): "))
                print("Generated Secure Password:", generate_secure_password(length))
            elif choice == 5:
                words = int(input("Enter the number of words for the memorable password: "))
                print("Generated Memorable Password:", generate_memorable_password(words))
            elif choice == 6:
                pw = input("Enter the password to check for palindrome: ")
                print("Is Palindrome:", is_palindrome_password(pw))
            elif choice == 7:
                print("Exiting Password Security Analyzer. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
