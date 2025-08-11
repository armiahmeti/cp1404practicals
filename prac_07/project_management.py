"""Project Management Program per CP1404 prac_07 spec."""
    from __future__ import annotations
    import sys
    from datetime import datetime
    from project import Project, DATE_FMT

    DEFAULT_FILE = "projects.txt"

    MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
>>> """


    def load_projects(filename: str = DEFAULT_FILE) -> list[Project]:
        projects: list[Project] = []
        with open(filename, "r", encoding="utf-8") as f:
            header = f.readline()  # discard header
            for line in f:
                line = line.strip()
                if not line:
                    continue
                projects.append(Project.from_tab_line(line))
        return projects


    def save_projects(filename: str, projects: list[Project]) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=f)
            for p in projects:
                print(p.to_tab_line(), file=f)


    def display_projects(projects: list[Project]) -> None:
        incomplete = sorted([p for p in projects if p.is_incomplete])
        complete = sorted([p for p in projects if p.is_complete])
        print("Incomplete projects:")
        for p in incomplete:
            print(f"  {p}")
        print("Completed projects:")
        for p in complete:
            print(f"  {p}")


    def filter_projects_by_date(projects: list[Project]) -> None:
        date_string = input(f"Show projects that start after date ({DATE_FMT.lower()}): ")
        try:
            after = datetime.strptime(date_string, DATE_FMT).date()
        except ValueError:
            print("Invalid date format.")
            return
        filtered = [p for p in projects if p.start_date >= after]
        for p in sorted(filtered, key=lambda x: x.start_date):
            print(p)


    def add_new_project(projects: list[Project]) -> None:
        print("Let's add a new project")
        name = input("Name: ").strip()
        date_string = input(f"Start date ({DATE_FMT.lower()}): ").strip()
        priority = int(input("Priority (1=high): ").strip())
        cost_estimate = float(input("Cost estimate: $").strip())
        completion_percentage = int(input("Percent complete: ").strip())
        start_date = datetime.strptime(date_string, DATE_FMT).date()
        projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


    def choose_project(projects: list[Project]) -> int | None:
        # Show indexed, sorted by name for stable selection
        for i, p in enumerate(projects):
            print(f"{i} {p}")
        try:
            choice = int(input("Project choice: ").strip())
        except ValueError:
            print("Invalid choice.")
            return None
        if 0 <= choice < len(projects):
            return choice
        print("Choice out of range.")
        return None


    def update_project(projects: list[Project]) -> None:
        idx = choose_project(projects)
        if idx is None:
            return
        project = projects[idx]
        print(project)
        try:
            new_percent_str = input("New Percentage: ").strip()
            new_priority_str = input("New Priority: ").strip()
            if new_percent_str != "":
                project.completion_percentage = int(new_percent_str)
            if new_priority_str != "":
                project.priority = int(new_priority_str)
        except ValueError:
            print("Invalid numeric input; no changes made.")


    def main():
        print("Welcome to Pythonic Project Management")
        try:
            projects = load_projects(DEFAULT_FILE)
            print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
        except FileNotFoundError:
            projects = []
            print("No default projects file found; starting with an empty list.")

        while True:
            choice = input(MENU).strip().lower()
            if choice == "l":
                filename = input("Filename to load: ").strip()
                try:
                    projects = load_projects(filename)
                    print(f"Loaded {len(projects)} projects from {filename}")
                except Exception as e:
                    print(f"Failed to load: {e}")
            elif choice == "s":
                filename = input("Filename to save to: ").strip() or DEFAULT_FILE
                try:
                    save_projects(filename, projects)
                    print(f"Saved {len(projects)} projects to {filename}")
                except Exception as e:
                    print(f"Failed to save: {e}")
            elif choice == "d":
                display_projects(projects)
            elif choice == "f":
                filter_projects_by_date(projects)
            elif choice == "a":
                try:
                    add_new_project(projects)
                except Exception as e:
                    print(f"Failed to add project: {e}")
            elif choice == "u":
                update_project(projects)
            elif choice == "q":
                resp = input(f"Would you like to save to {DEFAULT_FILE}? (y/N): ").strip().lower()
                if resp.startswith("y") and projects:
                    try:
                        save_projects(DEFAULT_FILE, projects)
                        print(f"Saved {len(projects)} projects to {DEFAULT_FILE}")
                    except Exception as e:
                        print(f"Failed to save: {e}")
                print("Thank you for using custom-built project management software.")
                sys.exit(0)
            else:
                print("Invalid option")    


    if __name__ == "__main__":
        main()
