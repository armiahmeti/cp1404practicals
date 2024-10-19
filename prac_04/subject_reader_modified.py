"""
CP1404 Practical - Adjusted Solution
Program to read and display subject details from file
"""

FILENAME = "subject_data.txt"

def main():
    """Read subject data from file and display them in a formatted manner."""
    subjects_data = load_subjects()
    show_subjects(subjects_data)

def load_subjects():
    """Load subject data from file and convert it into structured lists."""
    subjects = []
    with open(FILENAME) as file:
        for line in file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects

def show_subjects(subjects):
    """Display the subject details in a user-friendly format."""
    for subject in subjects:
        print(f"{subject[0]} is instructed by {subject[1]} and has {subject[2]} students")

main()
