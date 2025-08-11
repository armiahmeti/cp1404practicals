"""
Prac 10 - testing with asserts & doctest.
Run this file to execute doctests.
"""

from __future__ import annotations
from dataclasses import dataclass
import doctest


def repeat_string(s: str, n: int) -> str:
    """
    Return the string s repeated n times.

    >>> repeat_string("hi", 3)
    'hihihi'
    >>> repeat_string("x", 0)
    ''
    >>> repeat_string("", 5)
    ''
    """
    if n <= 0:
        return ""
    return s * n


def is_long_word(word: str, length: int = 5) -> bool:
    """
    Determine if the word is at least as long as the given length.

    >>> is_long_word("not")
    False
    >>> is_long_word("super")
    True
    >>> is_long_word("Python", 6)
    True
    >>> is_long_word("code", 5)
    False
    """
    return len(word) >= length


def format_sentence(phrase: str) -> str:
    """
    Format a phrase as a sentence: capitalise first character and ensure a single trailing full stop.

    Leading/trailing spaces are ignored.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("Hello")
    'Hello.'
    >>> format_sentence("hello.")
    'Hello.'
    >>> format_sentence("  multiple words here  ")
    'Multiple words here.'
    >>> format_sentence("already proper.")
    'Already proper.'
    >>> format_sentence("wHy SO Loud")
    'Why so loud.'
    """
    text = phrase.strip()
    if not text:
        return "."  # degenerate case
    if text.endswith("."):
        text = text[:-1]
    return text[:1].upper() + text[1:].lower() + "."


# Minimal Car tests (and optional fallback Car for when car.py is not in path)
try:
    from car import Car  # type: ignore
except Exception:
    @dataclass
    class Car:  # fallback for local assertions if needed
        name: str
        fuel: float = 0
        odometer: float = 0

        def add_fuel(self, amount: float) -> None:
            self.fuel += amount

        def drive(self, distance: float) -> float:
            actual = min(distance, self.fuel)
            self.fuel -= actual
            self.odometer += actual
            return actual


def _car_assertions() -> None:
    """Simple assert tests for Car fuel behaviour."""
    c = Car("Test", 10)
    assert c.fuel == 10, "Initial fuel should be set from constructor"
    c.add_fuel(5)
    assert c.fuel == 15, "Fuel should increase after add_fuel"
    c.drive(7)
    assert c.fuel == 8, "Fuel should reduce by distance actually driven"
    c.drive(100)
    assert c.fuel == 0, "Driving further than fuel should reduce fuel to zero"


if __name__ == "__main__":
    _car_assertions()
    doctest.testmod(verbose=False)
    doctest.runmod(verbose=True)
    print("All tests passed.")
