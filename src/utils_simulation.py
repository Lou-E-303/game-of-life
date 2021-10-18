import copy
from time import sleep

import utils_board


def set_initial_position(board):
    chance_cell_is_alive = 30  # Percent chance a given cell is alive
    board = utils_board.set_random_grid(board, chance_cell_is_alive)
    return board


def run_simulation(initial_board):
    new_board = copy.deepcopy(initial_board)
    while True:
        for i, row in enumerate(initial_board):
            for j, value in enumerate(row):
                neighbours = get_neighbours(initial_board, i, j)

                alive_neighbour_count = get_alive_neighbour_count(neighbours)

                if initial_board[i][j] == 1 and not (alive_neighbour_count == 2 or alive_neighbour_count == 3):
                    print("Row: " + str(i) + " Col: " + str(j) + " Living Neighbours: " + str(alive_neighbour_count) + " Setting dead!")
                    new_board[i][j] = 0
                if initial_board[i][j] == 0 and alive_neighbour_count == 3:
                    print("Row: " + str(i) + " Col: " + str(j) + " Living Neighbours: " + str(alive_neighbour_count) + " Setting alive!")
                    new_board[i][j] = 1

        sleep(1)
        utils_board.print_board(new_board)
        initial_board = copy.deepcopy(new_board)


def get_neighbours(initial_board, i, j):
    top_left = initial_board[(i-1 + 8) % 8][(j-1 + 8) % 8]
    top_middle = initial_board[(i-1 + 8) % 8][j]
    top_right = initial_board[(i-1 + 8) % 8][(j+1 + 8) % 8]

    left = initial_board[i][(j-1 + 8) % 8]
    right = initial_board[i][(j+1 + 8) % 8]

    bottom_left = initial_board[(i+1 + 8) % 8][(j-1 + 8) % 8]
    bottom_middle = initial_board[(i+1 + 8) % 8][j]
    bottom_right = initial_board[(i+1 + 8) % 8][(j+1 + 8) % 8]

    neighbours = [
        top_left,    top_middle,    top_right,
        left,                       right,
        bottom_left, bottom_middle, bottom_right
    ]

    return neighbours


def get_alive_neighbour_count(neighbours):
    neighbour_count = 0

    for i, neighbour in enumerate(neighbours):
        if neighbours[i] == 1:
            neighbour_count += 1

    return neighbour_count
