
from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only sometimes, based on reliability."""
        if randint(1, 100) >= self.reliability:
            distance = 0
        return super().drive(distance)
