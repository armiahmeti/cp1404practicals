"""
CP1404/CP5632 Practical
Car class with basic functionalities.
"""

class Automobile:
    """Represent an Automobile with fuel and odometer tracking."""

    def __init__(self, model_name="", initial_fuel=0):
        """Initialize an Automobile instance with a model name and starting fuel.
        
        model_name: str, the name of the automobile
        initial_fuel: int or float, initial fuel capacity (km per unit)
        """
        self.model_name = model_name
        self.fuel_capacity = initial_fuel
        self.odometer_reading = 0  # Tracks the total distance traveled by the car

    def __str__(self):
        """Return a string representation of the Automobile object."""
        return f"{self.model_name}, fuel={self.fuel_capacity}, odometer={self.odometer_reading}"

    def drive(self, distance):
        """Drive the automobile a given distance if fuel allows, and update odometer.
        
        distance: int or float, the distance to attempt driving
        """
        if distance <= 0:
            print("Drive distance must be positive.")
            return 0
        
        max_distance = min(distance, self.fuel_capacity)
        self.odometer_reading += max_distance
        self.fuel_capacity -= max_distance
        return max_distance

    def add_fuel(self, amount):
        """Add a specified amount of fuel to the automobile's tank.
        
        amount: int or float, amount of fuel to add
        """
        if amount > 0:
            self.fuel_capacity += amount
        else:
            print("Fuel amount to add must be positive.")
