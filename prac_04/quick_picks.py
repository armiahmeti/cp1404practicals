import random

PICK_COUNT = 6
LOW = 1
HIGH = 45

def main():
    total_picks = int(input("How many quick picks? "))
    while total_picks < 0:
        print("Invalid number of picks.")
        total_picks = int(input("How many quick picks? "))

    for _ in range(total_picks):
        pick = []
        while len(pick) < PICK_COUNT:
            rand_num = random.randint(LOW, HIGH)
            if rand_num not in pick:
                pick.append(rand_num)
        pick.sort()
        print(" ".join(f"{n:2}" for n in pick))

main()
