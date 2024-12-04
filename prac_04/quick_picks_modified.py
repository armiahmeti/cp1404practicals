"""
CP1404 Practical - Refined Solution
Quick Pick Lottery Ticket Generator
"""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_PICK = 6

def main():
    """Generate random quick pick lottery numbers."""
    number_of_picks = int(input("How many quick picks? "))
    
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in sorted(quick_pick)))

def generate_quick_pick():
    """Generate a quick pick with no repeated numbers."""
    return random.sample(range(MINIMUM, MAXIMUM + 1), NUMBERS_PER_PICK)

main()
