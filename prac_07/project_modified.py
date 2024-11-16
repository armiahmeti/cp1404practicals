
# project.py

from datetime import datetime

class Project:
    """Represents a project with a name, start date, priority, cost estimate, and completion status."""
    
    def __init__(self, name, start_date, priority, estimate, completion_percentage=0):
        """Initialize a Project instance with essential attributes."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = priority
        self.estimate = estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, "
                f"estimate: ${self.estimate:.2f}, completion: {self.completion_percentage}%")
    def update_estimate(self, new_estimate):
        return self.completion_percentage >=
    def is_completed(self):
        """Check if the project is fully completed."""
        return self.completion_percentage >= 100

    def update_completion(self, completion):
        """Update the completion percentage of the project."""
        if 0 <= completion <= 100:
            self.completion_percentage = completion

    def update_priority(self, new_priority):
        """Update the priority of the project."""
        self.priority = new_priority

    def __lt__(self, other):
        """Comparison method for sorting projects by priority."""
        return self.priority < other.priority

# Sample usage for testing
if __name__ == "__main__":
    project = Project("Sample Project", "01/01/2023", 1, 1000.00, 20)
    print(project)
    print("Completed:", project.is_completed())
