"""Taxi simulator using Taxi and SilverServiceTaxi classes."""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def list_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    list_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return choice
        print("Invalid taxi choice")
        return None
    except ValueError:
        print("Invalid taxi choice")
        return None


def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0.0
    current_index = None

    while True:
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").strip().lower()
        if choice == 'q':
            break
        elif choice == 'c':
            idx = choose_taxi(taxis)
            if idx is not None:
                current_index = idx
        elif choice == 'd':
            if current_index is None:
                print("You need to choose a taxi before you can drive")
            else:
                taxi = taxis[current_index]
                try:
                    distance = float(input("Drive how far? "))
                except ValueError:
                    distance = 0.0
                taxi.start_fare()
                taxi.drive(distance)
                trip_cost = taxi.get_fare()
                print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
                bill_to_date += trip_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    list_taxis(taxis)


if __name__ == "__main__":
    main()
