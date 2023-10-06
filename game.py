from turn import play_computer_turn, play_human_turn


def play_one_round(n):
    # This function processes the human turn.
    # Then process the computer turn.
    # Prints the number of coins left.
    n = play_human_turn(n)
    if n == 0:
        return 0
        

    n = play_computer_turn(n)
    if n == 0:
        return 0

    print("There are " + str(n) + " coins on the table.\n")
    return n


def play_game():
    print("Welcome to the countdown from 21 game!")
    print("There are 21 coins on table.")
    print("On each player's turn, you may remove 1, 2, or 3 coins.")
    print("If a player removes all the coins, they win.")
    print("It's your move.")

    coins = 21
    while coins > 0:
        coins = play_one_round(coins)


play_game()
