import servidor
from servidor.board import Board

if __name__ == "__main__":
    chess_board = Board()
    chess_board.create_board()
    chess_board.put_pieces(servidor.DEFAULT_WHITE_BOARD_MAP, servidor.DEFAULT_BLACK_BOARD_MAP)
    chess_board.print_board()