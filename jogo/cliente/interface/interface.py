import socket
import json
import cliente


class Interface:
	def __init__(self):
		self.connection = socket.socket()
		self.connection.connect((cliente.SERVER_ADDRESS, cliente.PORT))

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
		self.send_int(connection, size, cliente.INT_SIZE)
		connection.send(data)

	def receive_object(self, connection):
		"""1º: lê tamanho, 2º: lê dados."""
		size = self.receive_int(connection, cliente.INT_SIZE)
		data = b""
		while len(data) < size:
			chunk = connection.recv(size - len(data))
			if not chunk:
				raise ConnectionError("Connection closed before all data received")
			data += chunk
		return json.loads(data.decode('utf-8'))

	# ---------------------- game logic ------------------------------

	def _do_move(self) -> None:
		""" This method shows the interface that allows the player to make a move"""
		while True:
			option = input("Enter command (select): ").strip().lower()
			if option != "select":
				print("Unknown command. Type 'select' to pick a piece.")
				continue

			self.send_str(self.connection, cliente.SELECT)

			piece = input("Select the square of a piece of your colour (e.g. e2): ").strip()
			self.send_object(self.connection, piece)


			status = self.receive_object(self.connection)

			if status == cliente.EMPTY:
				print("That square is empty. Try again.")
			elif status == cliente.OPPO_COL:
				print("That piece is not yours. Try again.")
			elif status == cliente.VALID_SQUARE:
				print("Piece selected!")
				break
			else:
				print(f"Unexpected status: {repr(status)}")

		#sends destination
		self.send_str(self.connection, cliente.MOVE)
		print(self.receive_object(self.connection))
		destination = input("Enter the destination square (e.g. e4): ").strip()
		self.send_object(self.connection, destination)

	def _play(self) -> None:
		"""This method shows the interface of the overall game and statistics"""
		print(self.receive_object(self.connection))  # "PLEASE WAIT"
		print(self.receive_object(self.connection))  # "Welcome"

		while True:
			board = self.receive_object(self.connection)
			for line in board:
				print(line)

			print(self.receive_object(self.connection))  # turn message

			directive = self.receive_str(self.connection, cliente.COMMAND_SIZE)

			if directive == cliente.MOVE:
				self._do_move()
			elif directive == cliente.WAIT:
				print("Waiting for opponent...")
			else:
				print(f"Unexpected directive: {directive!r}")

			# Receive statistics AFTER the move has been made
			statistics = self.receive_object(self.connection)
			if statistics == cliente.CHECK:
				print("King is in Check!")
			elif statistics == cliente.CHECKMATE:
				print("The game is Over! (Checkmate)")
				break  # ← end the loop, game is over
			elif statistics == cliente.STALEMATE:
				print("The game is Over! (Stalemate)")
				break  # ← end the loop, game is over

	def execute(self):
		"""
		This is the base of the connection. If the player wants to queue up
		for a game they only need to type "play"
		"""
		print("Select an option:")
		connection_alive = True
		res = ""
		while res != ".":
			res = input("Command (play / '.' to quit): ").strip().lower()
			if res == "play":
				self.send_str(self.connection, cliente.PLAY)
				try:
					self._play()
				except (ConnectionResetError, ConnectionError, OSError) as e:
					print(f"Connection lost: {e}")
					connection_alive = False
					break

			if connection_alive:
				try:
					self.send_str(self.connection, cliente.END_OP)
				except OSError:
					pass

			self.connection.close()