"""
Loops exercises
"""

# a. Print all odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# b. Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# c. Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# d. Print n stars in one line
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

# e. Print n lines of increasing stars
for i in range(1, number_of_stars + 1):
    print('*' * i)
