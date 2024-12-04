
"""CP1404/CP5632 - Practical - Suggested Solution
Program to get password and print asterisks
"""

MINIMUM_LENGTH = 5

def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)

def get_password(minimum_length):
    """Get password, ensuring it meets the minimum_length requirement."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password

def print_asterisks(password):
    """Print asterisks for the length of the password."""
    print('*' * len(password))

main()
