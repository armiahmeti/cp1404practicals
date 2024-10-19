"""
CP1404 Practical - Password Checker
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
REQUIRES_SPECIAL = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\"


def main():
    """Get and validate a password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("	1 or more uppercase characters")
    print("	1 or more lowercase characters")
    print("	1 or more numbers")
    if REQUIRES_SPECIAL:
        print(f"	and 1 or more special characters:  {SPECIAL_CHARACTERS}")
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = sum(1 for c in password if c.islower())
    count_upper = sum(1 for c in password if c.isupper())
    count_digit = sum(1 for c in password if c.isdigit())
    count_special = sum(1 for c in password if c in SPECIAL_CHARACTERS)

    if count_lower and count_upper and count_digit and (not REQUIRES_SPECIAL or count_special):
        return True
    return False


main()
