from classes.pessoa import Pessoa
from classes.juridica import PessoaJuridica
from classes.fisica import PessoaFisica

pessoaUm = Pessoa("Projeto temporário", "Rua dos açores", "12345678910")
pessoaDois = Pessoa("Projeto temporário 2", "Vila do chaves", "23456789101")
pessoaTres = PessoaFisica("Bruno Henrique Guinerio", "Condomínio", "99999999999", "11111111111", "12042003")
pessoaQuatro = PessoaFisica("Nome qualquer de exemplo", "Passadina", "98765432198", "22222222222", "01091980")
pessoaCinco = PessoaJuridica("Empresa um", "São paulo", "78965412309", "87456321000190", "Empresa exemplo LTDA")
pessoaSeis = PessoaJuridica("Empresa dois", "Rio de Janeiro", "96325874191", "12365487000190", "Empresa exemplo 2 LTDA")
pessoas = [pessoaUm, pessoaDois, pessoaTres, pessoaQuatro, pessoaCinco, pessoaSeis]