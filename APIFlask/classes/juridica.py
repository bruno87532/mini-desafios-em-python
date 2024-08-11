from .pessoa import Pessoa
class PessoaJuridica(Pessoa):
    def __init__(self, nome, endereco, contato, cnpj, razaoSocial):
        self.cnpj = cnpj
        self.razaoSocial = razaoSocial
        super().__init__(nome, endereco, contato)