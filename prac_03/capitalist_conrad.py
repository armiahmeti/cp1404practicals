"""
Prac 03 - Capitalist Conrad
"""
import random

INITIAL_PRICE = 10.00
MIN_PRICE = 1.00
MAX_PRICE = 100.00
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
FILENAME = "capitalist_conrad.txt"
CURRENCY = "$"

price = INITIAL_PRICE
number_of_days = 0

with open(FILENAME, "w") as out_file:
    print(f"Starting price: {CURRENCY}{price:,.2f}", file=out_file)
    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1
        if random.randint(0, 1) == 1:
            price_change = price * random.uniform(0, MAX_INCREASE)
        else:
            price_change = -price * random.uniform(0, MAX_DECREASE)
        price += price_change
        print(f"On day {number_of_days} price is: {CURRENCY}{price:,.2f}", file=out_file)

print(f"Simulation finished after {number_of_days} days. Output written to {FILENAME}.")
