"""
Prac 03 - Password Checker
"""
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def is_valid_password(password: str) -> bool:
    if not (MIN_LENGTH <= len(password) <= MAX_LENGTH):
        return False
    count_lower = count_upper = count_digit = count_special = 0
    for ch in password:
        if ch.islower():
            count_lower += 1
        elif ch.isupper():
            count_upper += 1
        elif ch.isdigit():
            count_digit += 1
        elif ch in SPECIAL_CHARACTERS:
            count_special += 1
    if count_lower < 1 or count_upper < 1 or count_digit < 1:
        return False
    if SPECIAL_CHARS_REQUIRED and count_special < 1:
        return False
    return True

def main():
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("    1 or more uppercase characters")
    print("    1 or more lowercase characters")
    print("    1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"    and 1 or more special characters:  {SPECIAL_CHARACTERS}")
    while True:
        password = input("> ")
        if is_valid_password(password):
            print(f"Your {len(password)} character password is valid: {password}")
            break
        else:
            print("Invalid password!")

if __name__ == "__main__":
    main()
