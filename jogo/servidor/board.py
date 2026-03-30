import servidor
from servidor.pieces.piece import Piece
class Board:
    def __init__(self):
        self.board: list = []

    def create_board(self):
        self.board = [0] * 8

        for collumn in range(len(self.board)):
            self.board[collumn] = ["  "] * 8

    """_summary_
        Esta função insere as peças pretas e brancas no tabulerios

        @parametros
        board:list - matriz 8x8 representado o tabuleiro
        white_pieces:dict - dicionário com as pecas brancas
        black_pieces:dict - dicionário com as pecas pretas
    """
    def put_pieces(self, white_pieces: dict[str, list[Piece]], black_pieces: dict):
        for piece, squares in white_pieces.items():
            for square in squares:
                piece_pos = square.current_pos
                x, y = servidor.col_map[piece_pos[0]], 8 - int(piece_pos[1])
                self.board[y][x] = square
        for piece, squares in black_pieces.items():
            for square in squares:
                piece_pos = square.current_pos
                x, y = servidor.col_map[piece_pos[0]], 8 - int(piece_pos[1])
                self.board[y][x] = square

    def print_board(self):
        for i, row in enumerate(self.board):
            print(8 - i, end=": ")
            for j, col in enumerate(row):
                if col == "  ":
                    print(col, end=" ")
                else:
                    print(col.piece, end=" ")
            print("\n")
        print(
            " " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h")



