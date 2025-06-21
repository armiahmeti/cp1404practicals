"""
Email to Name Mapping
Estimate: 25 minutes
Actual: 30 minutes
"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email:
        default_name = extract_name(email)
        confirm = input(f"Is your name {default_name}? (Y/n) ")
        if confirm.strip().upper() not in ("Y", ""):
            default_name = input("Name: ")
        email_to_name[email] = default_name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    return " ".join(parts).title()

main()