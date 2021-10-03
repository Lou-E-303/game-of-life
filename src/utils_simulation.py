import utils_board


def set_initial_position(board):
    chance_cell_is_alive = 30  # Percent chance a given cell is alive
    board = utils_board.set_random_grid(board, chance_cell_is_alive)
    return board
