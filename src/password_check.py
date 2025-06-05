import random
import string
import math

# check if the password strong => length at least 8 chars, use upper and lowercase, use digits, use special characters
def is_strong_password(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    return has_upper and has_lower and has_digit and has_special

# check if password weak => i.e. not strong password
def is_weak_password(password):
    return not is_strong_password(password)

# sequential characters like abcd or 1234 => based on sorting
def has_sequential_chars(password, seq_len=4):
    for i in range(len(password) - seq_len + 1):
        segment = password[i:i + seq_len]
        if segment.isalpha() and segment == ''.join(sorted(segment)):
            return True
        if segment.isdigit() and segment == ''.join(sorted(segment)):
            return True
    return False

# password is in one of common passwords
def is_common_password(password):
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
    return password in common_passwords

# generate strong password => length can be specified
def generate_secure_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    while True:
        password = ''.join(random.choices(
            string.ascii_letters + string.digits + string.punctuation,
            k=length
        ))
        if is_strong_password(password):
            return password

# measure password entropy => describes the randomness of the password
# entropy = log2(size of character set \) * length
def password_entropy(password):
    char_set_size = 0
    if any(char.islower() for char in password):
        char_set_size += 26
    if any(char.isupper() for char in password):
        char_set_size += 26
    if any(char.isdigit() for char in password):
        char_set_size += 10
    if any( char in string.punctuation for char in password):
        char_set_size += len(string.punctuation)
    return 0 if char_set_size == 0 else len(password) * math.log2(char_set_size)

# number of character types in the password => uppercase, lowercase, digits, special characters
def character_type_count(password):
    return {
        "uppercase": sum(1 for char in password if char.isupper()),
        "lowercase": sum(1 for char in password if char.islower()),
        "digits": sum(1 for char in password if char.isdigit()),
        "special": sum(1 for char in password if char in string.punctuation)
    }

# number of special characters in the password
def count_special_characters(password):
    return sum(1 for char in password if char in string.punctuation)

# check if any spaces
def has_spaces(password):
    return " " in password

# rreverse password
def reverse_password(password):
    return password[::-1]

# mask password for display purposes => show first and last character hide rest with *
def mask_password(password):
    if len(password) <= 4:
        return "*" * len(password)
    return password[0] + "*" * (len(password) - 2) + password[-1]

# summary of everything
def password_summary(password):
    return {
        "is_strong": is_strong_password(password),
        "is_weak": is_weak_password(password),
        "has_sequential_chars": has_sequential_chars(password),
        "is_common": is_common_password(password),
        "entropy": password_entropy(password),
        "character_types": character_type_count(password),
        "special_char_count": count_special_characters(password),
        "has_spaces": has_spaces(password),
        "reversed": reverse_password(password),
        "masked": mask_password(password),
    }

# check for repeated characters in the password => variable threshold
def has_repeated_chars(password, threshold=3):
    return any(password.count(char) > threshold for char in set(password))

# password improvement suggestions
def suggest_password_improvements(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase the password length to at least 8 characters.")
    if not any(char.isupper() for char in password):
        suggestions.append("Add at least one uppercase letter.")
    if not any(char.islower() for char in password):
        suggestions.append("Add at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        suggestions.append("Include at least one digit.")
    if not any(char in string.punctuation for char in password):
        suggestions.append("Include at least one special character.")
    if has_sequential_chars(password):
        suggestions.append("Avoid sequential characters like 'abcd' or '1234'.")
    if has_repeated_chars(password):
        suggestions.append("Avoid repeated characters.")
    if is_common_password(password):
        suggestions.append("Avoid using common passwords.")

    return suggestions if suggestions else ["Your password is strong!"]

# memorable password generator => uses a list of words
def generate_memorable_password(words=4):
    word_list = [
        "apple", "banana", "cherry", "dragon", "elephant",
        "falcon", "grape", "honey", "island", "jungle"
    ]
    password = ''.join(random.choice(word_list).capitalize() for _ in range(words))
    special_char = random.choice(string.punctuation)
    digit = random.choice(string.digits)
    return f"{password}{special_char}{digit}"

# check if password palindrome
def is_palindrome_password(password):
    return password == password[::-1]

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
                password = input("Enter the password to check: ")
                print("Strong password:", is_strong_password(password))
            elif choice == 2:
                password = input("Enter the password to summarize: ")
                summary = password_summary(password)
                print("Password Summary:")
                for key, value in summary.items():
                    print(f"  {key}: {value}")
            elif choice == 3:
                password = input("Enter the password to improve: ")
                suggestions = suggest_password_improvements(password)
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
                password = input("Enter the password to check for palindrome: ")
                print("Is Palindrome:", is_palindrome_password(password))
            elif choice == 7:
                print("Exiting Password Security Analyzer. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
