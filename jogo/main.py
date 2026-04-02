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

        current_king = white_king if turno % 2 == 0 else black_king
        current_color = "w" if turno % 2 == 0 else "b"
        if current_king.is_checkmate(chess_board.board) == 1:
            winner = "Black" if turno % 2 == 0 else "White"
            print(f"Checkmate! {winner} wins!")
            break
        elif current_king.is_checkmate(chess_board.board) == 2:
            print("Stalemate!")
            break


        if current_king.is_in_check(chess_board.board):
            print("Check!")

        position = input("Escolha a posição da peça: ")
        x, y = servidor.letter.index(position[0]), 8 - int(position[1])
        current_sq = chess_board.board[y][x]

        if current_sq == "  ":
            print("No piece there!")
            continue

        if current_sq.piece[0] != current_color:
            print("That's not your piece!")
            continue

        piece = current_sq
        piece.check_available_moves(chess_board.board)
        print(piece.available_moves)

        new_pos = input("Select a square to move on to: ")
        piece.move(piece, new_pos, chess_board.board)
        turno += 1