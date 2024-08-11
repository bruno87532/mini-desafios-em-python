from flask import abort
class Pessoa:
    _id_Contador = 0
    def __init__(self, nome, endereco, contato):
        self.id = Pessoa._id_Contador
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        Pessoa._id_Contador += 1
    @staticmethod
    def localiza_pessoa(id, listaPessoas):
        for i in listaPessoas:
            if id == i.id:
                return i
        abort(404, "Página não encontrada")
    @classmethod
    def adicionaPessoa(cls, pessoa):
        campos = ["nome", "endereco", "contato"]
        if not all(campo in pessoa.keys() and pessoa[campo] for campo in campos):
            abort(400, "Dados insuficientes")
        novaPessoa = cls(pessoa["nome"], pessoa["endereco"], pessoa["contato"])
        return novaPessoa