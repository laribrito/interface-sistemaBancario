class Globo:
    def __init__(self):
        self.lista = []

    def adicionaCliente(self, cliente):
        self.lista.append(cliente)
    
    def getLista(self):
        return self.lista

g = Globo()
    

