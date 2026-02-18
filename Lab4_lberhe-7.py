"""
Program Name: Deal Cards
Author: Lewam Berhe
Purpose: Lab 4 programming assignment for CSCI-1511
Starter Code: None
Date: feburary 10, 2026
"""
import random
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["c", "h", "s", "d"]
num_cards = int(input("How many cards do you want? "))
deck = []
for v in values:
    for s in suits:
        deck.append(v + s)
hand = random.sample(deck, num_cards)
print("Your hand:")
for card in hand:
    print(card)
print("Total cards:", num_cards)

