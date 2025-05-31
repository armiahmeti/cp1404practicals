"""
CP1404/CP5632 - Practical - Suggested Solution
Temperature conversions
"""

# Note: this is a constant, so it is global, defined before main
MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def main():
    """Simple tool for converting temperatures."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye!")


def convert_celsius_to_fahrenheit(celsius):
    """Returns Fahrenheit for given Celsius."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Returns Celsius for given Fahrenheit."""
    return 5 / 9 * (fahrenheit - 32)


main()
