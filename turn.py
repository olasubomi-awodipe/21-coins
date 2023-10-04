import random


def play_human_turn(n):
    # 1. prompt user for their move
    x = int(input("Make a move(1, 2 or 3): "))

    while n >= 0:
        if x == 0:
            x = int(input("You have to take a coin. \nTry again(1,2 or 3)"))

        elif x < 0:
            x = int(input("You can't take a coin in the negative. \nTry again (1,2 or 3): "))
        elif x > 3:
            x = int(input("You can't make a move greater than 3. \nTry again(1, 2 or 3): "))
        elif x > n:
            x = int(input("You can't take more than the available number of coins. \nTry again: "))

    # 2. output number of coins after user's move
        else:
            n -= x
            print("There are " + str(n) + " coins on the table.")
            break

    # 3. If the human wins, indicate that and return 0
    if n == 0:
        print("Yay, you won, there are no coins on the table.")
        return 0
    else:
        return n

    # You must implement this function


def play_computer_turn(n):
    # 1. Make computer move
    c = n % 4

    # 2. If computer wins, indicate that and return 0
    if c == 0:
        c = random.randint(1, 3)
    print("The computer took " + str(c) + " coins.")

    if (n - c) == 0:
        print('Sorry, you lost!The computer won.')
        return 0

    # 3. return number of coins remaining
    else:
        return n - c

    # You must implement this function
