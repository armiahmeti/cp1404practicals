"""Guitar class for 'More Guitars!' exercise."""
from dataclasses import dataclass
from datetime import date


VINTAGE_AGE = 50


@dataclass(order=False)
class Guitar:
    name: str
    year: int
    cost: float

    def __str__(self) -> str:
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def is_vintage(self, asof: int | None = None) -> bool:
        if asof is None:
            asof = date.today().year
        return asof - self.year >= VINTAGE_AGE

    def __lt__(self, other: "Guitar") -> bool:
        # Sort by year (oldest first)
        return self.year < other.year
