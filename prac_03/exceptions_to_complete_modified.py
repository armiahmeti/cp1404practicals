"""
CP1404 Practical - Handling Exceptions
"""

finished = False
result = None
while not finished:
    try:
        result = int(input("Enter an integer: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Valid result is: {result}")
