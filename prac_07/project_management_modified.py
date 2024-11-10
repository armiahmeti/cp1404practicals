
# project_management.py

from project import Project
from datetime import datetime

def main():
    """Main program to manage projects through a menu system."""
    projects = load_projects("projects.txt")
    while True:
        choice = display_menu()
        if choice == "L":
            projects = load_projects(input("Filename to load from: "))
        elif choice == "S":
            save_projects(input("Filename to save to: "), projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            break
        else:
            print("Invalid option, please try again.")

def load_projects(filename):
    """Load projects from a text file and return a list of Project objects."""
    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            name, start_date, priority, estimate, completion = line.strip().split('\t')
            project = Project(name, start_date, int(priority), float(estimate), int(completion))
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save projects to a text file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.estimate}\t{project.completion_percentage}\n")

def display_menu():
    """Display menu and return user's choice."""
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects")
    print("- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
    return input(">>> ").upper()

def display_projects(projects):
    """Display completed and incomplete projects sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_completed()])
    complete = sorted([p for p in projects if p.is_completed()])
    print("Incomplete projects:")
    for project in incomplete:
        print(" ", project)
    print("Completed projects:")
    for project in complete:
        print(" ", project)

def filter_projects_by_date(projects):
    """Filter projects by user-specified start date and display those starting after the date."""
    date_string = input("Show projects starting after date (dd/mm/yyyy): ")
    date = datetime.strptime(date_string, "%d/%m/%Y")
    filtered_projects = [p for p in projects if p.start_date > date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)

def add_new_project(projects):
    """Add a new project to the list based on user input."""
    name = input("Project name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority (1-10): "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Completion percentage: "))
    projects.append(Project(name, start_date, priority, estimate, completion))

def update_project(projects):
    """Update an existing project's completion percentage or priority."""
    display_projects(projects)
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    completion = input("New completion percentage (leave blank to keep current): ")
    if completion:
        project.update_completion(int(completion))
    priority = input("New priority (leave blank to keep current): ")
    if priority:
        project.update_priority(int(priority))

if __name__ == "__main__":
    main()
