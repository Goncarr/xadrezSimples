import servidor
from servidor.board import Board

if __name__ == "__main__":
    chess_board = Board()
    chess_board.create_board()
    chess_board.put_pieces(servidor.DEFAULT_WHITE_BOARD_MAP, servidor.DEFAULT_BLACK_BOARD_MAP)
    while True:
        chess_board.print_board()
        position = input("Escolha a posição da peça")
        x, y =  servidor.col_map[position[0]], int(position[1]),
        current_pos = chess_board.board[y][x]
        if current_pos != "  ":
            piece = chess_board.board[y][x]
            print("\n\n\n\n\n")
            print(piece.check_available_moves(chess_board.board))
        else:
            print("uh oh")