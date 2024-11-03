"""
CP1404/CP5632 Practical - Modified Programming Language Class.
Defines a class to represent various characteristics of a programming language.
"""

class LanguageProfile:
    """Represent detailed information about a programming language."""

    def __init__(self, language_name, typing_discipline, supports_reflection, release_year):
        """Initialize a LanguageProfile instance with provided attributes."""
        self.language_name = language_name
        self.typing_discipline = typing_discipline
        self.supports_reflection = supports_reflection
        self.release_year = release_year

    def __str__(self):
        """Return a string representation of the LanguageProfile object."""
        reflection_status = "supports reflection" if self.supports_reflection else "does not support reflection"
        return (f"{self.language_name}, {self.typing_discipline} Typing, {reflection_status}, "
                f"First appeared in {self.release_year}")

    def is_dynamic(self):
        """Check if the language uses dynamic typing."""
        return self.typing_discipline.lower() == "dynamic"
