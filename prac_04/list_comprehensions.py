names_list = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names_list = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

first_letters = [n[0] for n in names_list]
print(first_letters)

initials = [fn.split()[0][0] + fn.split()[1][0] for fn in full_names_list]
print(initials)

a_only = [n for n in names_list if n.startswith('A')]
print(a_only)

lower_names = [fn.lower() for fn in full_names_list]
print(lower_names)

string_numbers = ['0', '10', '21', '3', '-7', '88', '9']
num_list = [int(s) for s in string_numbers]
print(num_list)

big_num_list = [n for n in num_list if n > 9]
print(big_num_list)
