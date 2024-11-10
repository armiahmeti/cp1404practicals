
# myguitars.py

from guitar import Guitar

def main():
    """Main program to load, display, and sort guitars."""
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)

def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    """Display all guitars in a list with vintage status."""
    print("Guitars loaded:")
    for guitar in guitars:
        vintage_status = "(Vintage)" if guitar.is_vintage() else ""
        print(f"{guitar} {vintage_status}")

def sort_guitars_by_year(guitars):
    """Sort guitars by year and display them in order."""
    guitars.sort()
    print("Guitars sorted by year:")
    display_guitars(guitars)

if __name__ == "__main__":
    main()
