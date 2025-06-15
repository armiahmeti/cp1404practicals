FILE = "subject_data.txt"

def main():
    subject_list = read_subjects()
    print_subjects(subject_list)

def read_subjects():
    subject_list = []
    with open(FILE) as file:
        for entry in file:
            data = entry.strip().split(',')
            data[2] = int(data[2])
            subject_list.append(data)
    return subject_list

def print_subjects(subject_list):
    for data in subject_list:
        print(f"{data[0]} is taught by {data[1]:12} and has {data[2]:3} students")

main()
