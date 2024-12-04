"""
CP1404/CP5632 Practical - Suggested Solution
Email to name dictionary
"""


def main():
    """Generate a dictionary that maps emails to corresponding names."""
    email_to_name = {}
    email = input("Please enter your email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.lower() != "y" and confirmation.strip()::
            name = input("Name: ")
        email_to_name.update({email: name})
        email = input("Please enter your email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract expected name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
