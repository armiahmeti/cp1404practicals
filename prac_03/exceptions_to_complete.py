"""
Prac 03 - Exceptions To Complete
"""
def get_valid_integer(prompt="Enter an integer: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; enter a whole number.")

def main():
    number = get_valid_integer()
    result = number * 2
    print(f"Double of {number} is {result}")
    print("Finished.")

if __name__ == "__main__":
    main()
