"""
Program Name: player
Author: Lewam Berhe
Purpose: Lab9 programming assignment for CSCI-1511
Starter Code: None
Date: March 24, 2026
"""

from coin import Coin
class Player:
    def __init__(self, name):
        self.name = name
        self.coin = Coin()
        self.score = 0

    def toss_coin(self):
        self.coin.toss()

    def get_coin_side(self):
        return self.coin.get_sideup()

    def add_point(self):
        """Increase the player's score by 1."""
        self.score += 1

    def get_score(self):
        """Return the player's current score."""
        return self.score