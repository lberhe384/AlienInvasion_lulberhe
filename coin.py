"""
Program Name: coin
Author: Lewam Berhe
Purpose: Lab9 programming assignment for CSCI-1511
Starter Code: None
Date: March 24, 2026
"""
import random

class Coin:
    def __init__(self):
        """Initialize the coin with a random side up (Heads or Tails)."""
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def toss(self):
        """Simulate tossing the coin and randomly set the side up."""
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        """Return the current side of the coin."""
        return self.__sideup