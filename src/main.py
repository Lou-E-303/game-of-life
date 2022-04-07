import utils_board
import utils_simulation

rows, columns = 8, 8

board = utils_board.setup_board(rows, columns)

board = utils_simulation.set_initial_position(board, 30)

utils_simulation.run_simulation(board)
