"""
CP1404/CP5632 Practical - Modified Guitar Collection Program
Program to collect and display guitar information using the Guitar class.
"""
from prac_06.modified_guitar import Guitar

def main():
    """Program to collect details of multiple guitars."""
    guitar_list = []

    print("Welcome to the Guitar Collection Program!")
    model_name = input("Enter the guitar name: ")
    while model_name != "":
        production_year = int(input("Enter the manufacture year: "))
        price = float(input("Enter the cost ($): "))
        new_guitar = Guitar(model_name, production_year, price)
        guitar_list.append(new_guitar)
        print(f"{new_guitar} has been added to your collection.")
        model_name = input("Enter the guitar name: ")

    # Display all guitars
    if guitar_list:
        print("
Here's a summary of your guitar collection:")
        for idx, guitar in enumerate(guitar_list, 1):
            vintage_status = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {idx}: {guitar.model_name:>20} ({guitar.manufacture_year}), "
                  f"worth ${guitar.price:10,.2f}{vintage_status}")
    else:
        print("You have no guitars in your collection.")

if __name__ == "__main__":
    main()
