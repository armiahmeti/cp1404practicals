"""
CP1404/CP5632 Practical - State names dictionary lookup
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

def main():
    state_code = input("Enter short state: ").strip().upper()
    while state_code:
        state_name = CODE_TO_NAME.get(state_code)
        if state_name:
            print(f"{state_code} is {state_name}")
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ").strip().upper()

main()