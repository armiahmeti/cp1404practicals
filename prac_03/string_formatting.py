"""
Prac 03 - String Formatting
"""

# Task 1
year = 1922
name = "Gibson L-5 CES"
price = 16035.999
print(f"{year} {name} for about ${price:,.0f}!")

# Task 2
for i in range(11):
    print(f"2 ^ {i:>2} is {2 ** i:>4}")
