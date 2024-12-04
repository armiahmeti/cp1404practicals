"""
CP1404 Practical - File Operations
"""

# Write name to file
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Read name from file and greet
with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Hi {name}!")

# Read numbers from file and add first two
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    result = first_number + second_number
    print(f"Sum of first two numbers: {result}")

# Sum all numbers from file
with open("numbers.txt", "r") as file:
    total = sum(int(line) for line in file)
print(f"Total of all numbers: {total}")
