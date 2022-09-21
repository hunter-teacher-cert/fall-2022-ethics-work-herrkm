# nim.py
# Kiana Herr
# CSCI 77800 Fall 2022
# collaborators: N/A
# consulted: N/A

print("Let's play Nim!\n")

# set initial stone quantity
n = 12

# set max number of stones to take
max_stones = 3

print(f"There are {n} stones in the bag. On your turn, you can take 1-{max_stones} stones.")
print("The player who takes the last stone wins!\n")

while n > 0:
    print(f"There are {n} stones left.")
    player_move = input("How many stones would you like to take?\n")

    # input validation: check if the input is a digit between 1 and max_stones but not more than n
    if not(player_move.isdigit()):
        print(f"Invalid move. Please enter a whole number between 1 and {max_stones}.")
        continue
    else:
        player_move = int(player_move)
        if player_move < 1 or player_move > max_stones:
            print(f"Invalid move. Please enter a whole number between 1 and {max_stones}.")
            continue
        elif player_move > n:
            print(f"Invalid move. You can't take more stones than are left in the bag.")
            continue
    
    # calculate new bag total
    n -= player_move
    print(f"There are {n} stones left.")

    # check for win
    if n == 0:
        print("Player wins! Congratulations!")
        break

    # computer player move: attempt to get in winning position (multiple of max + 1)
    # if impossible, take one stone
    elif n % (max_stones + 1) == 0:
        ai_move = 1
    else:
        ai_move = n % (max_stones + 1)
        
        # create situation where player can win to test player win scenario
        # ai_move = 1

    print(f"The computer has taken {ai_move} stones.")
    n -= ai_move
    
    # check for win
    if n == 0:
        print("There are 0 stones left.\nComputer wins! Better luck next time.")