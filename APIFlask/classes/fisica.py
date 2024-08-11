from .pessoa import Pessoa
class PessoaFisica(Pessoa):
    def __init__(self, nome, endereco, contato, cpf, dataNascimento):
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        super().__init__(nome, endereco, contato)