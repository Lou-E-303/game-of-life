import random


def setup_board(rows, columns):
    # TODO all of this would be so much easier with a Cell object
    board = [[0 for i in range(columns)] for j in range(rows)]
    return board


def print_board(board):
    print("\n")
    for i in board:
        print(i)
    print("\n")


def set_square(board, row_index, column_index, set_alive):
    try:
        board[row_index][column_index] = 1 if set_alive else 0
    except IndexError:
        print("Index out of bounds: Square (" + str(row_index) + ", " + str(column_index) + ") not set")

    return board


# Note: this is an ugly function and I am only using it for testing purposes - set_square should be the
# single source of truth for setting the state so as soon as I have the Sense HAT set up on my Pi to
# take user input, I will kill it with fire
def set_random_grid(board, chance_cell_is_alive):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if random.randint(1, 100) > chance_cell_is_alive:  # Since chance_cell_is_alive is a percentage
                board[i][j] = 0
            else:
                board[i][j] = 1
    return board
