def setup_board(rows, columns):
    board = [[0 for i in range(columns)] for j in range(rows)]
    return board


def print_board(board):
    for i in board:
        print(i)
    print("\n")


# TODO: Replace if statement with proper Python try/except
#  as this is currently a bit messy

def set_square(board, row_index, column_index, alive_or_dead):
    if (row_index <= len(board)) and (column_index <= len(board[0])):
        board[row_index][column_index] = 1 if alive_or_dead else 0
        return board
    else:
        print("Index out of bounds: Square (" + str(row_index) + ", " + str(column_index) + ") not set")
        return board
