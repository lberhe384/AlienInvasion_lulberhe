"""
Program Name: "Match Coins" game"
Author: Lewam Berhe
Purpose: Lab9 programming assignment for CSCI-1511
Starter Code: None
Date: March 24, 2026
"""
from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    rounds = 5  

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.name}: {side1}")
        print(f"{player2.name}: {side2}")

        if side1 == side2:
            print(f"{player1.name} wins this round!")
            player1.add_point()
        else:
            print(f"{player2.name} wins this round!")
            player2.add_point()

    print("\nFinal Scores:")
    print(f"{player1.name}: {player1.get_score()}")
    print(f"{player2.name}: {player2.get_score()}")

    if player1.get_score() > player2.get_score():
        print(f"{player1.name} wins the game!")
    elif player2.get_score() > player1.get_score():
        print(f"{player2.name} wins the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
