pessoas = []

class Pessoa:
    _id_Contador = 0
    def __init__(self, nome, endereco, contato):
        self.id = Pessoa._id_Contador
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        Pessoa._id_Contador += 1
        self.adicionaLista()
    def adicionaLista(self):
        pessoas.append(self)