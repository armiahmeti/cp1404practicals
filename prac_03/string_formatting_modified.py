"""
CP1404 Practical - Refined String Formatting Example
"""

# Example 1: Formatted string with a variable and format specifier
name = "Gibson L-5 CES"
year = 1922
cost = 16036.4
print(f"{year} {name} for around ${cost:,.0f}!")

# Example 2: Using a loop to print powers of two with formatted output
for exponent in range(11):
    print(f"2 ^ {exponent:>2} is {2 ** exponent:>4}")
