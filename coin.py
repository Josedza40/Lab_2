"""
Program Name: Match Coins Game - Coin Class
Author: Jose Daniel Zambrano
Purpose: Create a coin object that can be tossed and can store whether
         the coin is showing Heads or Tails.
Starter Code: None.
Date: 09/27/2026
"""

import random


class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        number = random.randint(0, 1)

        if number == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup