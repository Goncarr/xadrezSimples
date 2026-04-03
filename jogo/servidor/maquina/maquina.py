import socket
import json
import servidor
from servidor.lista_clientes.lista_clientes import ListaCliente
from servidor.matches.matchManager import MatchManager
from servidor.processa_cliente import ProcessaCliente


class Maquina:
    def __init__(self):
        self.clientes = ListaCliente()
        self.s = socket.socket()
        self.s.bind(('', servidor.PORT))
        self.matchManager = MatchManager()

    # ---------------------- interaction with sockets ------------------------------
    def receive_int(self, connection, n_bytes: int) -> int:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next integer read from the current connection
        """
        data = connection.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)


    def send_int(self, connection, value: int, n_bytes: int) -> None:
        """
        :param value: The integer value to be sent to the current connection
        :param n_bytes: The number of bytes to send
        """
        connection.send(value.to_bytes(n_bytes, byteorder="big", signed=True))


    def receive_str(self, connection, n_bytes: int) -> str:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next string read from the current connection
        """
        data = connection.recv(n_bytes)
        return data.decode()


    def send_str(self, connection, value: str) -> None:
        """
        :param value: The string value to send to the current connection
        """
        connection.connection.send(value.encode())


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


    # ---------------------- interaction with sockets ------------------------------

    def execute(self):
        self.s.listen(1)
        print("Waiting for clients on port " + str(servidor.PORT))
        while True:  # Loop infinito para múltiplos clients
            print("On accept...")
            connection, address = self.s.accept()
            print("Client", address, "connected")
            self.clientes.connect(connection, address)
            print(self.clientes.clientes)
            processo_cliente = ProcessaCliente(connection, address, self.clientes, self.matchManager)
            processo_cliente.start()  # Arranca thread após ligação



if __name__ == "__main__":
    m = Maquina()
    m.execute()