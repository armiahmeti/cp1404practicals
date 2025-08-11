"""UnreliableCar that sometimes refuses to drive."""
from __future__ import annotations
import random


class UnreliableCar:
    def __init__(self, name: str, fuel: float, reliability: float):
        try:
            from car import Car  # type: ignore
            self.__class__ = type(self.__class__.__name__, (Car,), dict(self.__class__.__dict__))
            super().__init__(name, fuel)
        except Exception:
            self.name = name
            self.fuel = fuel
            self.odometer = 0
        self.reliability = float(reliability)

    def drive(self, distance: float) -> float:
        roll = random.uniform(0, 100)
        if roll < self.reliability:
            try:
                return super().drive(distance)  # type: ignore[misc]
            except Exception:
                driven = max(0.0, min(distance, self.fuel))
                self.fuel -= driven
                self.odometer = getattr(self, 'odometer', 0) + driven
                return driven
        return 0.0
