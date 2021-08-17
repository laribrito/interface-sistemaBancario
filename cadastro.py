from PyQt5 import QtWidgets, uic
from pessoaJ import PessoaJ
from pessoaF import PessoaF
from lista import g

class Cadastro(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("telas/cadastro.ui", self)
        self.lista = []

        self.cadastrar = self.findChild(QtWidgets.QPushButton, "cadastrar")
        self.cadastrar.clicked.connect(self.fazerCadastro)

        self.getDocumento = self.findChild(QtWidgets.QLineEdit, "doc") #cpf/cnpj
        self.getTelefone = self.findChild(QtWidgets.QLineEdit, "telefone")
        self.getNome = self.findChild(QtWidgets.QLineEdit, "nome")
        self.getEndereco = self.findChild(QtWidgets.QLineEdit, "endereco")
        self.getJuridica = self.findChild(QtWidgets.QRadioButton, "juridica")
        self.getFisica = self.findChild(QtWidgets.QRadioButton, "fisica")

    def fazerCadastro(self):
        self.documento = self.getDocumento.text()
        self.telefone = self.getTelefone.text()
        self.nome = self.getNome.text()
        self.endereco = self.getEndereco.text()
        if self.documento == "":
            msgbox = QtWidgets.QMessageBox()
            msgbox.critical(self, "Preencha todos os campos", "Insira um CPF/CNPJ\nSeu burro")
        elif self.telefone == "":
            msgbox = QtWidgets.QMessageBox()
            msgbox.critical(self, "Preencha todos os campos", "Insira um telefone\nSeu burro")
        elif self.nome == "":
            msgbox = QtWidgets.QMessageBox()
            msgbox.critical(self, "Preencha todos os campos", "Insira um Nome/Razão Social\nSeu burro")
        elif self.endereco == "":
            msgbox = QtWidgets.QMessageBox()
            msgbox.critical(self, "Preencha todos os campos", "Insira um endereço\nSeu burro")
        else:
            if self.getJuridica.isChecked():
                cliente = PessoaJ(self.documento, self.nome, self.telefone, self.endereco)
            elif self.getFisica.isChecked():
                cliente = PessoaF(self.documento, self.nome, self.telefone, self.endereco)
            g.adicionaCliente(cliente)


            msgbox = QtWidgets.QMessageBox()
            msgbox.information(self, "Cadastrado com sucesso", f"O Número da sua conta é: {cliente.getNumero()}\nVocê tem R$ {(-1)*cliente.getLimite()} de Crédito Especial!")
            self.close()


        
    