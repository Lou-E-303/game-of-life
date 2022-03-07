import random


def setup_board(rows, columns):
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


def set_random_grid(board, percent_chance_cell_is_alive):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if random.randint(1, 100) > percent_chance_cell_is_alive:
                board[i][j] = 0
            else:
                board[i][j] = 1
    return board
