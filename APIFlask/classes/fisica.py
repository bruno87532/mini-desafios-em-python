from .pessoa import Pessoa
from flask import abort
class PessoaFisica(Pessoa):
    def __init__(self, nome, endereco, contato, cpf, dataNascimento):
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        super().__init__(nome, endereco, contato)
    @classmethod
    def adicionaPessoa(cls, pessoa):
        campos = ["nome", "endereco", "contato", "cpf", "dataNascimento"]
        if not all(campo in pessoa.keys() and pessoa[campo] for campo in campos):
            abort(400, "Dados insuficientes")
        novaPessoa = cls(pessoa["nome"], pessoa["endereco"], pessoa["contato"], pessoa["cpf"], pessoa["dataNascimento"])
        return novaPessoa
    def editaPessoa(self, dados):
        campos = ["nome", "endereco", "contato", "cpf", "dataNascimento"]
        if not all(campo in dados.keys() and dados[campo] for campo in campos):
            abort(400, "Dados insuficentes")
        for campo in campos:
            setattr(self, campo, dados[campo])