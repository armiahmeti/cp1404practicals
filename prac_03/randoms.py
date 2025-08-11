"""
Prac 03 - Random Numbers exploration
"""
import random

print(random.randint(5, 20))        # line 1
print(random.randrange(3, 10, 2))   # line 2
print(random.uniform(2.5, 5.5))     # line 3

# Answers:
# Line 1: integers 5–20 inclusive.
# Line 2: sequence 3, 5, 7, 9. No 4 possible.
# Line 3: float 2.5–5.5 inclusive.

one_to_hundred = random.randint(1, 100)
print(one_to_hundred)
