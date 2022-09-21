# gol.py
# Kiana Herr
# CSCI 77800 Fall 2022
# collaborators: N/A
# consulted: N/A


# RULES: 
# Living cells with 2 or 3 neighbors survive.
# Dead cells with 3 neighbors are born.
# All other cells die or remain dead.
# All births and deaths occur simultaneously.



import random
from re import L


# creates an n x n board
def build_random_board(n = 10, p = .5):
    '''
    build_empty_board(n)
    Returns an n x n nested list with rate of "alive" cells determined by float p.
    int n: dimensions of square 2d list, default 10
    float p: probability of cell being "alive." Between 0 and 1, default .5
    '''

    # create empty board
    board = [['-' for i in range(n)] for j in range(n)]

    # bring cells to life at probability p
    for row in range(n):
        for col in range(n):
            if random.random() <= p:
                board[row][col] = 'X'

    return board


# prints a 2d list board
def print_board(board):
    '''
    print_board(board)
    Takes a 2d list and prints it in an easy to read format.
    '''
    for row in board:
        for item in row:
            print(item, end = " ")
        print()

# counts the number of living neighbors of each cell
def count_neighbors(board, r, c):
    '''
    count_neighbors(board, r, c)
    Returns the number of living neighbors of board[r][c].
    '''
    count = 0
    # check row before and after, but not outside board bounds
    for row in range(max(0, r - 1), min(r + 2, len(board))):
        for col in range(max(0, c - 1), min(c + 2, len(board[row]))):
            if not(row == r and col == c):
                # print(f"({row},{col})")
                if board[row][col] == 'X':
                    count += 1
    return count

# gets the next generation status of a cell
def get_next_gen(board, r, c):
    '''
    get_next_gen(board, r, c)
    Returns the cell (r, c)'s next generation status based on
    the number of neighbors currently alive.
    '''
    live_neighbors = count_neighbors(board, r, c)
    if board[r][c] == '-':
        if live_neighbors == 3:
            return 'X'
        else:
            return '-'
    else:
        if live_neighbors == 2 or live_neighbors == 3:
            return 'X'
        else:
            return '-'

# gets the next generation board
def generate_next_board(board):
    '''
    Creates the next generation of the board according to 
    CGOL rules.
    '''
    new_board = [['-' for i in range(len(board[0]))] for j in range(len(board))]
    for row in range(len(new_board)):
        for col in range(len(new_board[row])):
            new_board[row][col] = get_next_gen(board, row, col)
    
    return new_board


test = build_random_board()
print("Gen 0:")
print_board(test)
# print("\nNumber of neighbors to cell (3, 2):")
# print(count_neighbors(test, 3, 2))
# print("Next generation of cell (3, 2):")
# print(get_next_gen(test, 3, 2))

# print("\nNumber of neighbors to cell (0, 0):")
# print(count_neighbors(test, 0, 0))
# print("Next generation of cell (0, 0):")
# print(get_next_gen(test, 0, 0))

# print("\nNumber of neighbors to cell (9, 5):")
# print(count_neighbors(test, 9, 5))
# print("Next generation of cell (9, 5):")
# print(get_next_gen(test, 9, 5))

print("Gen 1:")
test1 = generate_next_board(test)
print_board(test1)