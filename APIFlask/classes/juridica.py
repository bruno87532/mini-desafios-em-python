from .pessoa import Pessoa
from flask import abort
class PessoaJuridica(Pessoa):
    def __init__(self, nome, endereco, contato, cnpj, razaoSocial):
        self.cnpj = cnpj
        self.razaoSocial = razaoSocial
        super().__init__(nome, endereco, contato)
    @classmethod
    def adicionaPessoa(cls, pessoa):
        campos = ["nome", "endereco", "contato", "cnpj", "razaoSocial"]
        if not all(campo in pessoa.keys() and pessoa[campo] for campo in campos):
            abort(400, "Dados insuficientes")
        novaPessoa = cls(pessoa["nome"], pessoa["endereco"], pessoa["contato"], pessoa["cnpj"], pessoa["razaoSocial"])
        return novaPessoa