import queue
import json
import socket
import threading
import servidor
from servidor.matches.match import Match


class MatchManager:
    def __init__(self):
        self.waiting_queue = queue.Queue()  # Players waiting for a game
        self.active_matches = []            # List of Match objects

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

    # ---------------------- match management ------------------------------

    def add_player(self, player_socket):
        """
        This method verifies the queue. If no one is there, the player will wait,
        if not, it will grab both players and start a game
        """
        if self.waiting_queue.empty():
            self.waiting_queue.put(player_socket)
            return None
        else:
            opponent = self.waiting_queue.get()
            new_match = Match(opponent, player_socket)

            #This allows to check which players are currently playing
            self.active_matches.append(new_match)
            match_thread = threading.Thread(target=new_match.start_game, daemon=True)
            match_thread.start()
            return new_match