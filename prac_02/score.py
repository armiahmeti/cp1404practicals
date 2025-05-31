"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status, with function
"""


# Note boundary conditions (50 should be a pass, not > 50)
# Note efficiency and nesting; use the fewest number of if/elif as possible

def main()
:
    """Get a numeric score and evaluate and print its result."""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    """Evaluate score and return performance label."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

