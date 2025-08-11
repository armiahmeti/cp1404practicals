"""
Prac 03 - Files
"""
def write_name():
    name = input("Name: ")
    out_file = open("name.txt", "w")
    print(name, file=out_file)
    out_file.close()

def read_and_greet():
    in_file = open("name.txt", "r")
    name = in_file.read().strip()
    in_file.close()
    print(f"Hi {name}!")

def sum_first_two_numbers():
    with open("numbers.txt", "r") as f:
        first = int(f.readline())
        second = int(f.readline())
    print(first + second)

def sum_all_numbers():
    total = 0
    with open("numbers.txt", "r") as f:
        for line in f:
            total += int(line.strip())
    print(total)

if __name__ == "__main__":
    pass
