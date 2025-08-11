"""Band class for association example (Band has Musicians)."""
from __future__ import annotations

class Band:
    def __init__(self, name: str):
        self.name = name
        self.musicians = []

    def add(self, musician) -> None:
        self.musicians.append(musician)

    def __str__(self) -> str:
        members = ", ".join(str(m) for m in self.musicians)
        return f"{self.name} ({members})"

    def play(self) -> None:
        for m in self.musicians:
            # Expect Musician to have name and instruments list,
            # and instrument objects implement __str__ nicely.
            instruments = getattr(m, "instruments", [])
            if instruments:
                print(f"{m.name} is playing: {instruments[0]}")
            else:
                print(f"{m.name} needs an instrument!")
