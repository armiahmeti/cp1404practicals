
# guitar.py

class Guitar:
    """Represents a Guitar with a name, year, and cost attributes."""

    def __init__(self, name, year, cost):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Calculate the age of the guitar from the current year."""
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is considered vintage (older than 50 years)."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Comparison method for sorting guitars by year."""
        return self.year < other.year

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

# Sample usage for testing
if __name__ == "__main__":
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(guitar)
    print("Vintage:", guitar.is_vintage())
