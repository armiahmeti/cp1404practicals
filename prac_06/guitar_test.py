"""
CP1404 Practical Practical Exercise: Student Version
Basic manual tests for Guitar class
"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2017


def run_manual_tests():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print( f"{guitar.name} get_age() - Expecting {95}. Returned {guitar.get_age()}")
    print( f"{other.name} get_age() - Expecting {5}. Returned {other.get_age()}")
    print( )
    print( f"{guitar.name} is_vintage() - Expecting {True}. Returned {guitar.is_vintage()}")
    print( f"{other.name} is_vintage() - Expecting {False}. Returned {other.is_vintage()}")


if __name__ == '__main__':
    run_manual_tests()
