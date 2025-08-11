"""
Prac 03 - Exceptions Demo
"""
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid (not an integer). Try again.")

def main():
    numerator = get_int("Enter the numerator: ")
    denominator = get_int("Enter the denominator: ")
    while denominator == 0:
        print("Cannot divide by zero.")
        denominator = get_int("Enter the denominator (non-zero): ")
    result = numerator / denominator
    print(f"{numerator} / {denominator} = {result}")
    print("Finished.")

if __name__ == "__main__":
    main()

# Q1: ValueError when non-integer input.
# Q2: ZeroDivisionError when denominator=0.
# Q3: Avoid by re-prompting denominator until != 0.
