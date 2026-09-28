"""
Program Name: Match Coins Game
Author: Jose Daniel Zambrano
Purpose: Run a Match Coins game between two players. Each player tosses
         a coin and wins or loses coins depending on whether the sides match.
Starter Code: None.
Date: 09/27/2026
"""

from player import Player


def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    play = input("\nDo you want to toss the coins? (y/n): ")

    while play.lower() == "y":

        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            print("\n...It's a Match! Player 1 wins a coin.")
            player1.win_coin()
            player2.lose_coin()

        else:
            print("\n...No Match! Player 2 wins a coin.")
            player2.win_coin()
            player1.lose_coin()

        print()
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        play = input("\nDo you want to toss the coins again? (y/n): ")

    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 finished with more coins!")

    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 finished with more coins!")

    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()