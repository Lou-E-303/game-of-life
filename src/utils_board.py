def setup_board(rows, columns):
    board = [[0 for i in range(columns)] for j in range(rows)]
    return board


def print_board(board):
    for i in board:
        print(i)
    print("\n")


def set_square(board, row_index, column_index, set_alive):
    try:
        board[row_index][column_index] = 1 if set_alive else 0
    except IndexError:
        print("Index out of bounds: Square (" + str(row_index) + ", " + str(column_index) + ") not set")

    return board


