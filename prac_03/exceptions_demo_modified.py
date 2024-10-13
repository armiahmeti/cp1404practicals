"""
CP1404 Practical - Exception Handling Demo
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
else:
    print(f"Result: {result}")
