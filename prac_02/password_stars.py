"""
CP1404/CP5632 - Practical - Suggested Solution
Get a password with minimum length and display asterisks
"""

MINIMUM_LENGTH = 4


def version_1():
    """Get a password of valid size and print asterisks."""
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")

    print('*' * len(password))


# version_1()


def main():
    """Prompt user for a password and print asterisks."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Prompt for a valid password meeting the minimum length."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_asterisks(password_text):
    """Display asterisks equal to the password's length."""
    print('*' * len(password_text))


main()
