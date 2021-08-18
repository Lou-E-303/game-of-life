import utils_board

rows = 8
columns = 8
board = utils_board.setup_board(rows, columns)

utils_board.print_board(board)
utils_board.set_square_alive(board, 0, 0)
utils_board.print_board(board)
