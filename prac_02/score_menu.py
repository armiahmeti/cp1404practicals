
"""CP1404/CP5632 - Practical - Suggested Solution
Convert temperatures between files
This also contains a function to create the data file to begin with
"""

import random

def main():
    """Convert input file of one temperature unit to output file of another unit."""
    with open("temps_input.txt", "r") as input_file, open("temps_output.txt", "w") as output_file:
        for line in input_file:
            result = convert_fahrenheit_to_celsius(float(line))
            print(result, file=output_file)

def create_input_file(quantity):
    """Write random temperatures to file."""
    with open("temps_input.txt", "w") as temperatures_file:
        for _ in range(quantity):
            temperature = random.uniform(-200, 200)
            temperatures_file.write(f"{temperature}\n")

def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

main()
