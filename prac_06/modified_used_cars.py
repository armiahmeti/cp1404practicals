"""
CP1404/CP5632 Practical - Modified Client code for Automobile class.
This script demonstrates basic usage of the Automobile class.
"""
from prac_06.modified_car import Automobile

def main():
    """Demo test code to showcase the Automobile class."""
    # Create a new automobile instance and drive it a short distance
    user_vehicle = Automobile("User's Vehicle", 180)
    user_vehicle.drive(30)
    print(f"Remaining fuel: {user_vehicle.fuel_capacity}")
    print(user_vehicle)

    # Create a limo instance and perform some operations
    limo_vehicle = Automobile("Limo", 100)
    limo_vehicle.add_fuel(20)
    print(f"Updated fuel level for Limo: {limo_vehicle.fuel_capacity}")
    limo_vehicle.drive(115)
    print(limo_vehicle)

if __name__ == "__main__":
    main()
