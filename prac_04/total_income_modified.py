"""
CP1404 Practical - Refined Solution
Program to calculate cumulative total income over months
"""

def main():
    """Calculate and display income report for the given number of months."""
    monthly_incomes = []
    months_count = int(input("How many months of income to enter? "))

    for month in range(1, months_count + 1):
        income = float(input(f"Enter income for month {month}: "))
        monthly_incomes.append(income)

    print_income_report(monthly_incomes)


def print_income_report(monthly_incomes):
    """Generate and display a formatted income report."""
    print("\nIncome Summary\n-------------")
    cumulative_total = 0
    for month, income in enumerate(monthly_incomes, 1):
        cumulative_total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Cumulative Total: ${cumulative_total:10.2f}")


main()
