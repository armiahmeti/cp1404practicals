"""
CP1404 Practical
List comprehensions examples
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# List comprehension to get initials from names
first_initials = [name[0] for name in names]
print(first_initials)

# List comprehension for full initials from full names
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# List comprehension for names starting with 'A'
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# TODO: convert all full names to lowercase
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

# List comprehension to convert string numbers to integers
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(num) for num in almost_numbers]
print(numbers)

# List comprehension for numbers greater than 9
big_numbers = [num for num in numbers if num > 9]
print(big_numbers)
