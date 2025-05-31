# sales_bonus.py
# Program to calculate and display a user's bonus based on sales

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
