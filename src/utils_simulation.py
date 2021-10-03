import utils_board


def set_initial_position(board):
    chance_cell_is_alive = 30  # Percent chance a given cell is alive
    board = utils_board.set_random_grid(board, chance_cell_is_alive)
    return board


def run_simulation(initial_board):
    new_board = initial_board
    while True:
        for i, row in enumerate(initial_board):
            for j, value in enumerate(row):
                # Get neighbours
                # Count no. of alive neighbours
                # If Alive...
                    # If alive neighbours <= 3 or <= 4...
                        # Kill it
                # If Dead...
                    # If alive neighbours == 3...
                            # Set alive

        utils_board.print_board(new_board)


def get_neighbours(initial_board):
    # Do stuff

def get_alive_neighbour_count(neighbours):
    # Do stuff
