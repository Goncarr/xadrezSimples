import json
import socket

import servidor
from servidor.board import Board


class Match:
    def __init__(self, player_white, player_black):
        self.white = player_white
        self.black = player_black
        self.status = None
        self.player_turn = 0
        # self.board = Board() # Your chess logic instance

    def receive_str(self, connect, n_bytes: int) -> str:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next string read from the current connection
        """
        data = connect.recv(n_bytes)
        return data.decode()


    def send_str(self, connect, value: str) -> None:
        connect.send(value.encode())


    def send_int(self, connect: socket.socket, value: int, n_bytes: int) -> None:
        connect.send(value.to_bytes(n_bytes, byteorder="big", signed=True))


    def receive_int(self, connect: socket.socket, n_bytes: int) -> int:
        data = connect.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)

    def send_object(self, connection, obj):
        """1º: envia tamanho, 2º: envia dados."""
        data = json.dumps(obj).encode('utf-8')
        size = len(data)
        self.send_int(connection, size, servidor.INT_SIZE)  # Envio do tamanho
        connection.send(data)  # Envio do objeto


    def receive_object(self, connection):
        """1º: lê tamanho, 2º: lê dados."""
        size = self.receive_int(connection, servidor.INT_SIZE)  # Recebe o tamanho
        data = connection.recv(size)  # Recebe o objeto
        return json.loads(data.decode('utf-8'))

    def start_game(self):
        message = "Welcome"
        print(message)
        print(self.white)
        print(self.black)
        self.send_object(self.white, message)
        self.send_object(self.black, message)
        chess_board = Board()
        chess_board.create_board()
        chess_board.put_pieces(servidor.DEFAULT_WHITE_BOARD_MAP, servidor.DEFAULT_BLACK_BOARD_MAP)
        black_king = servidor.bking
        white_king = servidor.wking
        while True:
            self.send_object(self.white, chess_board.simple_print_board())
            self.send_object(self.black, chess_board.simple_print_board())
            current_king = white_king if self.player_turn % 2 == 0 else black_king
            current_color = "w" if self.player_turn % 2 == 0 else "b"

            if current_color == "w":
                self.send_object(self.white, "It's White's turn!")
                self.send_object(self.black, "It's White's turn!")

                self.send_str(self.white, servidor.MOVE)
                self.send_str(self.black, servidor.WAIT)

                request_type = self.receive_str(self.white, servidor.COMMAND_SIZE)
                print(request_type)
                if request_type == servidor.SELECT:
                    piece = self.receive_object(self.white)
                    print(piece)
                    x, y = servidor.letter.index(piece[0]), 8 - int(piece[1])
                    current_sq = chess_board.board[y][x]
                    if current_sq == "  ":
                        self.send_object(self.white, servidor.EMPTY)
                        continue
                    elif current_sq.piece[0] != current_color:
                        self.send_object(self.white, servidor.OPPO_COL)
                        continue
                    else:
                        self.send_object(self.white, servidor.VALID_SQUARE)
                        break
                        #piece = current_sq
                        #piece.check_available_moves(chess_board.board)
                else:
                    print("ops")
            else:
                self.send_object(self.white, "It's Black's turn!")
                self.send_object(self.black, "It's Black's turn!")

                self.send_str(self.white, servidor.WAIT)
                self.send_str(self.black, servidor.MOVE)

                request_type = self.receive_str(self.black, servidor.COMMAND_SIZE)
                if request_type == servidor.SELECT:
                    piece = self.receive_object(self.black)
                    x, y = servidor.letter.index(piece[0]), 8 - int(piece[1])
                    current_sq = chess_board.board[y][x]
                    if current_sq == "  ":
                        self.send_object(self.black, servidor.EMPTY)
                        continue
                    elif current_sq.piece[0] != current_color:
                        self.send_object(self.black, servidor.OPPO_COL)
                        continue
                    else:
                        self.send_object(self.black, servidor.VALID_SQUARE)
                        break
                        # piece = current_sq
                        # piece.check_available_moves(chess_board.board)
