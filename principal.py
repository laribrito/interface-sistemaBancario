from PyQt5 import QtWidgets, uic
from cadastro import Cadastro
from deposito import Deposito

class Principal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("telas/inicio.ui", self)
        self.show()

        self.telaCadastro = Cadastro()
        self.cadastro = self.findChild(QtWidgets.QPushButton, "cadastro")
        self.cadastro.clicked.connect(self.exibirCadastro)

        self.telaDeposito = Deposito()
        self.deposito = self.findChild(QtWidgets.QPushButton, "deposito")
        self.deposito.clicked.connect(self.exibirDeposito)
    
    def exibirCadastro(self):
        self.telaCadastro.show()

    def exibirDeposito(self):
        self.telaDeposito.show()
        