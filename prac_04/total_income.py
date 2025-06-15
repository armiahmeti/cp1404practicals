def main():
    earnings = []
    month_count = int(input("How many months? "))
    for m in range(1, month_count + 1):
        amount = float(input(f"Enter income for month {m}: "))
        earnings.append(amount)
    show_report(earnings)

def show_report(earnings):
    print("\nIncome Summary\n--------------")
    running_total = 0
    for idx, earning in enumerate(earnings, 1):
        running_total += earning
        print(f"Month {idx:2} - Income: ${earning:10.2f} Total: ${running_total:10.2f}")

main()
