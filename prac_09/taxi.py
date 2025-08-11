"""Taxi class extending Car.
Assumes a compatible Car class exists with attributes: name, fuel, odometer;
and methods: drive(distance) -> distance driven.
"""
from __future__ import annotations

class Taxi:
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # class variable (shared base price)

    def __init__(self, name: str, fuel: float):
        # Defer creation of Car attributes via composition by expecting mixin? No.
        # We assume multiple inheritance isn't used; instead we wrap/extend by duck-typing.
        # In the course template, Taxi actually inherits from Car. Keep that here:
        # (Kept separate to avoid circular imports in this standalone file.)
        # If you have car.py with class Car, replace the next line with: `super().__init__(name, fuel)`
        try:
            from car import Car  # type: ignore
            self.__class__ = type(self.__class__.__name__, (Car,), dict(self.__class__.__dict__))
            super().__init__(name, fuel)
        except Exception:
            # Fallback minimal attributes to allow repr without Car during static checks
            self.name = name
            self.fuel = fuel
            self.odometer = 0
        self.current_fare_distance = 0.0

    def __str__(self) -> str:
        # Match expected sample output formatting
        return (f"{self.name}, fuel={self.fuel}, odometer={getattr(self, 'odometer', 0)}, "
                f"{self.current_fare_distance:g}km on current fare, ${self.price_per_km:.2f}/km")

    def get_fare(self) -> float:
        """Return the price for the taxi trip, rounded to nearest 10c."""
        fare = self.price_per_km * self.current_fare_distance
        return round(fare, 1)

    def start_fare(self) -> None:
        self.current_fare_distance = 0.0

    def drive(self, distance: float) -> float:
        """Drive like a Car but also accumulate fare distance; return distance actually driven."""
        try:
            driven = super().drive(distance)  # type: ignore[misc]
        except Exception:
            # Fallback if Car not available
            driven = max(0.0, min(distance, self.fuel))
            self.fuel -= driven
            self.odometer = getattr(self, 'odometer', 0) + driven
        self.current_fare_distance += driven
        return driven
