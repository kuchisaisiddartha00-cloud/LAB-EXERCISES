# Program 16: Dice Simulator Using Random Module
import random

while True:
    command = input("Press Enter to roll the dice, or type q to quit: ").strip().lower()
    if command == "q":
        print("Thanks for playing!")
        break
    die_one = random.randint(1, 6)
    die_two = random.randint(1, 6)
    print(f"You rolled: {die_one} and {die_two}")
    print("Total:", die_one + die_two)
