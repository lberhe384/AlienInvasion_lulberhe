"""
Program Name: Dice Rolling Terms 
Author: Lewam Berhe
Purpose: Lab_5 CSCI-1511
Starter Code: None
Date: Feburary 17, 2026
"""
import random

while True:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total = roll1 + roll2

    print("\nroll 1:", roll1)
    print("roll 2:", roll2)
    print("Total:", total)

    if roll1 == 1 and roll2 == 1:
        print("Snake Eyes")

    elif (roll1 == 1 and roll2 == 2) or (roll1 == 2 and roll2 == 1):
        print("Ace Caught a Deuce")

    elif roll1 == 2 and roll2 == 2:
        print("Little Joe from Kokomo")

    elif (roll1 == 1 and roll2 == 4) or (roll1 == 4 and roll2 == 1) or \
         (roll1 == 2 and roll2 == 3) or (roll1 == 3 and roll2 == 2):
        print("Little Phoebe")

    elif roll1 == 3 and roll2 == 3:
        print("Jimmy Hicks from the Sticks")

    elif (roll1 == 6 and roll2 == 1) or (roll1 == 1 and roll2 == 6):
        print("Six Ace")

    elif roll1 == 4 and roll2 == 4:
        print("Eighter from Decatur")

    elif (roll1 == 3 and roll2 == 6) or (roll1 == 6 and roll2 == 3) or \
         (roll1 == 4 and roll2 == 5) or (roll1 == 5 and roll2 == 4):
        print("Nina from Pasadena")

    elif roll1 == 5 and roll2 == 5:
        print("Puppy Paws")

    elif (roll1 == 6 and roll2 == 5) or (roll1 == 5 and roll2 == 6):
        print("Six Five no Jive")

    elif roll1 == 6 and roll2 == 6:
        print("Boxcars")

    again = input("Roll again? (y/n): ")
    if again.lower() != "y":
        break