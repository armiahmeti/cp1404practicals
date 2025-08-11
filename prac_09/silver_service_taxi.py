"""SilverServiceTaxi extending Taxi with fanciness multiplier and flagfall."""
from __future__ import annotations
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50  # class variable

    def __init__(self, name: str, fuel: float, fanciness: float):
        super().__init__(name, fuel)
        # Multiply base price per km by fanciness; use class var base so global taxi price changes flow through
        self.price_per_km = Taxi.price_per_km * float(fanciness)

    def get_fare(self) -> float:
        # Base fare (rounded to 10c in Taxi) + flagfall (multiple of 10c, so remains on 10c grid)
        return super().get_fare() + self.flagfall

    def __str__(self) -> str:
        return super().__str__() + f" plus flagfall of ${self.flagfall:.2f}"
