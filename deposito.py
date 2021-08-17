from PyQt5 import QtWidgets, uic
from lista import g

class Deposito(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("telas/deposito.ui", self)
        
        self.depositar = self.findChild(QtWidgets.QPushButton, "depositar")
        self.depositar.clicked.connect(self.fazerDeposito)

        self.getConta = self.findChild(QtWidgets.QLineEdit, "conta")
        self.getValor = self.findChild(QtWidgets.QLineEdit, "valor")

    def fazerDeposito(self):
        self.conta = int(self.getConta.text())
        self.valor = float(self.getValor.text())
        if self.conta == "":
            msgbox = QtWidgets.QMessageBox()
            msgbox.critical(self, "Preencha todos os campos", "Insira uma conta\nSeu burro")
        elif self.valor == "":
            msgbox = QtWidgets.QMessageBox()
            msgbox.critical(self, "Preencha todos os campos", "Insira um valor\nSeu burro")
        else:
            nEncontrou = True
            lista = g.getLista()
            for conta in lista:
                if conta.getNumero() == self.conta:
                    nEncontrou = False
                    conta.testarLimite()
                    tst = conta.depositar(self.valor)
                    #recebe e testa o código de erro
                    if tst == 1:
                        msgbox = QtWidgets.QMessageBox()
                        msgbox.critical(self, "Preencha todos os campos", "Você inseriu um valor negativo\nSeu burro")
                    else:
                        msgbox = QtWidgets.QMessageBox()
                        msgbox.information(self, "Sucesso", "Deposito realizado com sucesso")
                        self.close()
            if nEncontrou:
                msgbox = QtWidgets.QMessageBox()
                msgbox.critical(self, "Preencha todos os campos", "A conta que você digitou não foi cadastrada ainda\nSeu burro")
                    

