import socket
import json
import cliente

class Interface:
	def __init__(self):
		self.connection = socket.socket()
		self.connection.connect((cliente.SERVER_ADDRESS,cliente.PORT))

###
	# ----- enviar e receber strings ----- #
	def receive_str(self,connect, n_bytes: int) -> str:
		"""
		:param n_bytes: The number of bytes to read from the current connection
		:return: The next string read from the current connection
		"""
		data = connect.recv(n_bytes)
		return data.decode()

	def send_str(self,connect, value: str) -> None:

		connect.send(value.encode())

	def send_int(self,connect:socket.socket, value: int, n_bytes: int) -> None:

		connect.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

	def receive_int(self,connect: socket.socket, n_bytes: int) -> int:

		data = connect.recv(n_bytes)
		return int.from_bytes(data, byteorder='big', signed=True)


	def send_object(self,connection, obj):
		"""1º: envia tamanho, 2º: envia dados."""
		data = json.dumps(obj).encode('utf-8')
		size = len(data)
		self.send_int(connection, size, cliente.INT_SIZE)         # Envio do tamanho
		connection.send(data)              		# Envio do objeto

	def receive_object(self,connection):
		"""1º: lê tamanho, 2º: lê dados."""
		size = self.receive_int(connection, cliente.INT_SIZE)  	# Recebe o tamanho
		data = connection.recv(size)       			# Recebe o objeto
		return json.loads(data.decode('utf-8'))
	###


	def execute(self):
		print("Selecione uma opção: ")
		res =""
		while res!=".":
			print("Qual é o cálculo que quer efetuar? play ('.' para fim)")
			res:str = input()
			if res =="play":
				self.send_str(self.connection, cliente.PLAY)
				print(self.receive_object(self.connection))
				print(self.receive_object(self.connection))
				while True:
					board = self.receive_object(self.connection) # Receives the board
					for line in board:
						print(line)
					print(self.receive_object(self.connection)) # Receives
					turno = self.receive_str(self.connection, cliente.COMMAND_SIZE)
					if turno == cliente.MOVE:
						while True:
							option = input("Seleciona uma opção: ")
							if option == "select":
								option = cliente.SELECT
								self.send_str(self.connection, option)
								piece = input("Select the space of a piece of your color: ")
								self.send_object(self.connection, piece)
								square_status = self.receive_object(self.connection)
								if square_status == cliente.EMPTY:
									print("This square is empty!")
									break
								elif square_status == cliente.OPPO_COL:
									print("This piece is not yours!")
									break
								elif square_status == cliente.VALID_SQUARE:
									print("Choose an available move from this list!")
									break
							else:
								print("asfcf")



					else:
						print("I can wait")

		self.send_str(self.connection, cliente.END_OP)
