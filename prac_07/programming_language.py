"""ProgrammingLanguage class for prac_07 (extended with pointer arithmetic)."""
from dataclasses import dataclass


@dataclass(order=False)
class ProgrammingLanguage:
    name: str
    typing: str                 # "Dynamic" or "Static"
    reflection: bool
    year: int
    pointer_arithmetic: bool    # new field

    def __str__(self) -> str:
        reflect = "Yes" if self.reflection else "No"
        ptr = "Yes" if self.pointer_arithmetic else "No"
        return (f"{self.name}, {self.typing} Typing, Reflection: {reflect}, "
                f"Year: {self.year}, Pointer Arithmetic: {ptr}")

    def is_dynamic(self) -> bool:
        return self.typing.strip().lower() == "dynamic"

    def supports_pointer_arithmetic(self) -> bool:
        return self.pointer_arithmetic
