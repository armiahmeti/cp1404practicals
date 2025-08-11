"""Project class and utilities for Project Management program.

Time estimate: 3–4 hours including design, implementation, and testing.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime


DATE_FMT = "%d/%m/%Y"


@dataclass(order=False)
class Project:
    name: str
    start_date: date
    priority: int
    cost_estimate: float
    completion_percentage: int

    def __str__(self) -> str:
        return (f"{self.name}, start: {self.start_date.strftime(DATE_FMT)}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    # Sort by priority ascending (1 = highest)
    def __lt__(self, other: "Project") -> bool:
        return self.priority < other.priority

    @property
    def is_complete(self) -> bool:
        return self.completion_percentage >= 100

    @property
    def is_incomplete(self) -> bool:
        return not self.is_complete

    @classmethod
    def from_tab_line(cls, line: str) -> "Project":
        # name	start_date	priority	cost_estimate	completion_percentage
        name, start, priority, cost, completion = [p.strip() for p in line.split("\t")]
        start_date = datetime.strptime(start, DATE_FMT).date()
        return cls(name, start_date, int(priority), float(cost), int(completion))

    def to_tab_line(self) -> str:
        return "\t".join([
            self.name,
            self.start_date.strftime(DATE_FMT),
            str(self.priority),
            f"{self.cost_estimate}",
            str(self.completion_percentage),
        ])
