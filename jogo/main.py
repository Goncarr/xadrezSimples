import servidor
from servidor.board import Board

if __name__ == "__main__":
    chess_board = Board()
    chess_board.create_board()
    chess_board.put_pieces(servidor.DEFAULT_WHITE_BOARD_MAP, servidor.DEFAULT_BLACK_BOARD_MAP)
    turno = 0
    black_king = servidor.bking
    white_king = servidor.wking
    while True:
        chess_board.print_board()
        if turno % 2 == 0:
            white_king.is_checked(chess_board.board)
        else:
            black_king.is_checked(chess_board.board)

        position = input("Escolha a posição da peça")
        x, y =  servidor.letter.index(position[0]), 8 - int(position[1])
        current_pos = chess_board.board[y][x]
        if current_pos != "  ":
            piece = current_pos
            piece.check_available_moves(chess_board.board)
            print(piece.available_moves)
            new_pos = input("Select a square to move on to: ")
            piece.move(piece, new_pos, chess_board.board)

        else:
            print("uh oh")