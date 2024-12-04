"""
CP1404/CP5632 Practical - Modified Testing for Guitar Class
Enhanced test cases for Guitar class functionalities.
"""
from prac_06.modified_guitar import Guitar

YEAR_REFERENCE = 2017

def run_tests():
    """Perform tests on Guitar class methods."""
    model = "Gibson L-5 CES"
    production_year = 1922
    price = 16035.40

    main_guitar = Guitar(model, production_year, price)
    second_guitar = Guitar("New Age Guitar", 2012, 1512.9)

    print(f"{main_guitar.model_name} get_age() - Expected {95}. Got {main_guitar.get_age()}")
    print(f"{second_guitar.model_name} get_age() - Expected {5}. Got {second_guitar.get_age()}")
    
    # Testing is_vintage method
    print(f"{main_guitar.model_name} is_vintage() - Expected True. Got {main_guitar.is_vintage()}")
    print(f"{second_guitar.model_name} is_vintage() - Expected False. Got {second_guitar.is_vintage()}")

if __name__ == "__main__":
    run_tests()
