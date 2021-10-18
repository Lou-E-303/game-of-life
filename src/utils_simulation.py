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
                neighbours = get_neighbours(initial_board, i, j)

                alive_neighbour_count = get_alive_neighbour_count(neighbours)

                if initial_board[i][j] == 1 and (3 <= alive_neighbour_count <= 4):
                    new_board[i][j] = 0
                if initial_board[i][j] == 0 and alive_neighbour_count == 3:
                    new_board[i][j] = 1

        utils_board.print_board(new_board)


# TODO currently this errors because we haven't handled wrapping - this is the next step
# The best way is probably going to be conditional assignment of top_left, top_middle etc...

def get_neighbours(initial_board, i, j):
    top_left = initial_board[i-1][j-1]
    top_middle = initial_board[i-1][j]
    top_right = initial_board[i-1][j+1]
    left = initial_board[i][j-1]
    right = initial_board[i][j+1]
    bottom_left = initial_board[i+1][j-1]
    bottom_middle = initial_board[i+1][j]
    bottom_right = initial_board[i+1][j+1]

    neighbours = [
        initial_board[i-1][j-1], initial_board[i-1][j], initial_board[i-1][j+1],
        initial_board[i][j-1],                          initial_board[i][j+1],
        initial_board[i+1][j-1], initial_board[i+1][j], initial_board[i+1][j+1]
    ]

    return neighbours


def get_alive_neighbour_count(neighbours):
    neighbour_count = 0

    for i, neighbour in enumerate(neighbours):
        if neighbours[i] == 1:
            neighbour_count += 1

    return neighbour_count