"""
CP1404 Practical - Random Numbers Example
"""

import random

# Generating random numbers
print(random.randint(5, 20))  # random integer between 5 and 20 inclusive
print(random.randrange(3, 10, 2))  # random number between 3 and 9, step 2
print(random.uniform(2.5, 5.5))  # random float between 2.5 and 5.5

# Random number between 1 and 100
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
