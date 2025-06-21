"""
Wimbledon Winners Data
Estimate: 30 minutes
Actual: 35 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_WINNER = 2

def main():
    data = load_data(FILENAME)
    champions, countries = process_data(data)
    display(champions, countries)

def load_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()  # skip header
        return [line.strip().split(",") for line in file]

def process_data(data):
    champions = {}
    countries = set()
    for row in data:
        countries.add(row[INDEX_COUNTRY])
        champions[row[INDEX_WINNER]] = champions.get(row[INDEX_WINNER], 0) + 1
    return champions, countries

def display(champions, countries):
    print("Wimbledon Champions:")
    for champ, wins in champions.items():
        print(f"{champ} {wins}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()