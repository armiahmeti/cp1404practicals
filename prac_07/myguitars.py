"""Manage Guitar objects: load, display, sort, add, and save to CSV."""
from guitar import Guitar

GUITARS_CSV = "guitars.csv"


def load_guitars(filename: str) -> list[Guitar]:
    guitars: list[Guitar] = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 3:
                    # Skip malformed lines
                    continue
                name, year_str, cost_str = parts
                # Skip header-like rows
                if not year_str.isdigit():
                    continue
                guitars.append(Guitar(name, int(year_str), float(cost_str)))
    except FileNotFoundError:
        pass
    return guitars


def display_guitars(guitars: list[Guitar], title: str = "Guitars"):
    print(title + ":")
    for i, g in enumerate(guitars):
        vintage_tag = " (vintage)" if g.is_vintage() else ""
        print(f" {i:>2}. {g}{vintage_tag}")
    if not guitars:
        print(" (none)")


def add_new_guitars() -> list[Guitar]:
    print("\nAdd new guitars (blank name to stop)")
    new_guitars: list[Guitar] = []
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars


def save_guitars(filename: str, guitars: list[Guitar]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for g in guitars:
            print(f"{g.name},{g.year},{g.cost}", file=f)


def main():
    guitars = load_guitars(GUITARS_CSV)
    display_guitars(guitars, title="Loaded guitars")

    guitars.sort()
    display_guitars(guitars, title="Sorted by year (oldest to newest)")

    new = add_new_guitars()
    if new:
        guitars.extend(new)
        guitars.sort()
        save_guitars(GUITARS_CSV, guitars)
        print(f"Saved {len(guitars)} guitars to {GUITARS_CSV}")
    else:
        print("No new guitars added; nothing saved.")


if __name__ == "__main__":
    main()
