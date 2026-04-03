class ListaCliente:
    def __init__(self):
        self.clientes = []

    def connect(self, connection, address):
        cliente = [connection, address]
        self.clientes.append(cliente)

    def disconnect(self, address):
        for cliente in self.clientes:
            if cliente[1] == address:
                self.clientes.remove(cliente)