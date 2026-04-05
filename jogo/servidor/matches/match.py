import json
import socket
import threading

import servidor
from servidor.board import Board


class Match(threading.Thread):
    def __init__(self, player_white, player_black):
        super().__init__()
        self.white = player_white
        self.black = player_black
        self.status = None
        self.player_turn = 0

    # ---------------------- interaction with sockets ------------------------------

    def receive_int(self, connect: socket.socket, n_bytes: int) -> int:
        data = b""
        while len(data) < n_bytes:
            chunk = connect.recv(n_bytes - len(data))
            if not chunk:
                raise ConnectionError("Connection closed before all data received")
            data += chunk
        return int.from_bytes(data, byteorder='big', signed=True)

    def send_int(self, connect: socket.socket, value: int, n_bytes: int) -> None:
        connect.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

    def receive_str(self, connect, n_bytes: int) -> str:
        data = b""
        while len(data) < n_bytes:
            chunk = connect.recv(n_bytes - len(data))
            if not chunk:
                raise ConnectionError("Connection closed before all data received")
            data += chunk
        return data.decode()

    def send_str(self, connect, value: str) -> None:
        connect.send(value.encode())

    def send_object(self, connection, obj) -> None:
        """1º: envia tamanho, 2º: envia dados."""
        data = json.dumps(obj).encode('utf-8')
        size = len(data)
        self.send_int(connection, size, servidor.INT_SIZE)
        connection.send(data)

    def receive_object(self, connection):
        """1º: lê tamanho, 2º: lê dados."""
        size = self.receive_int(connection, servidor.INT_SIZE)
        data = b""
        while len(data) < size:
            chunk = connection.recv(size - len(data))
            if not chunk:
                raise ConnectionError("Connection closed before all data received")
            data += chunk
        return json.loads(data.decode('utf-8'))

    # ---------------------- match logic ------------------------------

    def _broadcast(self, message) -> None:
        """Sends a message to both players."""
        self.send_object(self.white, message)
        self.send_object(self.black, message)

    def _current_player(self):
        """Defines which player plays (White always starts in this case)"""
        return self.white if self.player_turn % 2 == 0 else self.black

    def _current_color(self) -> str:
        """Identifies the color of the grids piece"""
        return "w" if self.player_turn % 2 == 0 else "b"

    def _notify_turn(self) -> None:
        """Sends a message to both clients indicating which player is playing currently"""
        label = "White" if self._current_color() == "w" else "Black"
        self._broadcast(f"It's {label}'s turn!")

    def _request_move(self, board: Board):
        """Request for the current player to indicate a pice to move"""
        current = self._current_player()
        color = self._current_color()
        waiting = self.black if color == "w" else self.white

        self.send_str(current, servidor.MOVE)
        self.send_str(waiting, servidor.WAIT)

        while True:
            # Verifies if player wants to select a piece
            # (Later this will include card selection or forfeit)
            command = self.receive_str(current, servidor.COMMAND_SIZE)
            print(f"[DEBUG] command={repr(command)}")

            if command != servidor.SELECT:
                self.send_object(current, servidor.INVALID_COMMAND)
                continue

            #coordinates of the piece
            piece_coord = self.receive_object(current)
            print(f"[DEBUG] Received piece_coord: {repr(piece_coord)}")

            x = servidor.letter.index(piece_coord[0])
            y = 8 - int(piece_coord[1])
            origin_sq = board.board[y][x]

            # Updating the player with the square's status
            if origin_sq == "  ":
                self.send_object(current, servidor.EMPTY)
                continue
            if origin_sq.piece[0] != color:
                self.send_object(current, servidor.OPPO_COL)
                continue

            self.send_object(current, servidor.VALID_SQUARE)
            print(f"[DEBUG] Sent VALID_SQUARE, waiting for MOVE command")

            # Player selects the space to move onto
            command = self.receive_str(current, servidor.COMMAND_SIZE)
            print(f"[DEBUG] Received move command: {repr(command)}")

            if command != servidor.MOVE:
                self.send_object(current, servidor.INVALID_COMMAND)
                continue

            origin_sq.check_available_moves(board.board)
            moves = origin_sq.available_moves
            self.send_object(current, moves)

            dest_coord = self.receive_object(current)
            print(f"[DEBUG] Received destination: {repr(dest_coord)}")

            dx = dest_coord[0]  # Ex: f
            dy = int(dest_coord[1])  # Ex: 5
            origin_sq.move(origin_sq, [dx, dy], board.board)
            return

    def start_game(self) -> None:
        try:
            # Welcoming and server print
            self._broadcast("Welcome")
            print(f"Match started: {self.white} vs {self.black}")

            #prints out the borad with the pieces already inserted
            board = Board()
            board.create_board()
            board.put_pieces(servidor.DEFAULT_WHITE_BOARD_MAP, servidor.DEFAULT_BLACK_BOARD_MAP)

            while True:
                black_king = servidor.bking
                white_king = servidor.wking
                #checks which king is checked/checkmated
                check_king = white_king if self.player_turn % 2 == 1 else black_king

                # Send board and turn message
                self._broadcast(board.simple_print_board())
                self._notify_turn()

                # Send directive (MOVE/WAIT) and process the move
                self._request_move(board)

                # Verifying in what condition the king is
                statistics = servidor.ACTIVE

                if check_king.is_checkmate(board.board) == 1:
                    statistics = servidor.CHECKMATE
                elif check_king.is_checkmate(board.board) == 2:
                    statistics = servidor.STALEMATE
                elif check_king.is_in_check(board.board):
                    statistics = servidor.CHECK

                # Updating clients of the conditions of the game
                self._broadcast(statistics)

                if statistics in (servidor.CHECKMATE, servidor.STALEMATE):
                    break  # Game finishes

                self.player_turn += 1

    # These conditions verify if something wrong came with any of the players
    # connections
        except (ConnectionResetError, ConnectionError, OSError) as e:
            print(f"Match ended due to connection error: {e}")
        finally:
            self._close_connections()

    def _close_connections(self) -> None:
        for conn in (self.white, self.black):
            try:
                conn.close()
            except OSError:
                pass