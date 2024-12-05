"""
CP1404/CP5632 Practical - Modified Guitar Class
Class representing a Guitar with methods to calculate age and vintage status.
"""

CURRENT_YEAR_ESTIMATE = 2017
VINTAGE_THRESHOLD = 50

class Guitar:
    """Class to represent a guitar with its specifications."""

    def __init__(self, model_name="", manufacture_year=0, price=0):
        """Initialize a Guitar instance with model name, year, and cost."""
        self.model_name = model_name
        self.manufacture_year = manufacture_year
        self.price = price

    def __str__(self):
        """Return a formatted string representation of a Guitar."""
        return f"{self.model_name} ({self.manufacture_year}) : ${self.price:,.2f}"

    def get_age(self):
        """Calculate the age of the guitar from the current year estimate."""
        return CURRENT_YEAR_ESTIMATE - self.manufacture_year

    def is_vintage(self):
        """Determine if the guitar qualifies as vintage."""
        return self.get_age() >= VINTAGE_THRESHOLD
