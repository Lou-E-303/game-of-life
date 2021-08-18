def setup_board(rows, columns):
    board = [[0 for i in range(columns)] for j in range(rows)]
    return board


def print_board(board):
    print("\n")
    for i in board:
        print(i)
    print("\n")


def set_square_alive(board, row_index, column_index):
    board[row_index][column_index] = 1
    return board


def set_square_dead(board, row_index, column_index):
    board[row_index][column_index] = 0
    return board
