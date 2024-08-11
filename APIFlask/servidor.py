from flask import Flask, jsonify, request, abort
from main import pessoas
from classes.pessoa import Pessoa
from classes.fisica import PessoaFisica
from classes.juridica import PessoaJuridica
servidor = Flask(__name__)

@servidor.errorhandler(404)
def naoEncontrado(erro):
    return jsonify({"Erro": str(erro)}), 404
@servidor.errorhandler(400)
def dadosInsuficientes(erro):
    return jsonify({"Erro": str(erro)}), 400
@servidor.route("/api/pessoas/")
def exibePessoas():
    listaPessoas = [i.__dict__ for i in pessoas]
    return jsonify(listaPessoas)
@servidor.route("/api/pessoas/<int:id>/")
def detalhaPessoa(id):
    pessoa = Pessoa.localiza_pessoa(id, pessoas)
    return jsonify(pessoa.__dict__)
@servidor.route("/api/pessoas/", methods=["POST"])
def adicionaPessoa():
    if not request.data:
        abort(400, "Dados insuficientes")
    pessoa = request.get_json()
    print(pessoa)
    pessoaFisica = ["nome", "endereco", "contato", "cpf", "dataNascimento"]
    if "cpf" in pessoa.keys():
        for i in pessoaFisica:
            if not(i in pessoa and pessoa[i]):
                abort(400, "Dados insuficientes")
        pessoaFisica = PessoaFisica(pessoa["nome"], pessoa["endereco"], pessoa["contato"], pessoa["cpf"], pessoa["dataNascimento"])
        pessoas.append(pessoaFisica)
        return jsonify({"id": pessoaFisica.id, "url": f"/api/pessoas/{pessoaFisica.id}"})
    pessoaJuridica = ["nome", "endereco", "contato", "cnpj", "razaoSocial"]
    if "cnpj" in pessoa.keys():
        for i in pessoaJuridica:
            if not(i in pessoa and pessoa[i]):
                abort(400, "Dados insuficientes")
        pessoaJuridica = PessoaJuridica(pessoa["nome"], pessoa["endereco"], pessoa["contato"], pessoa["cnpj"], pessoa["razaoSocial"])
        pessoas.append(pessoaJuridica)
        return jsonify({"id": pessoaJuridica.id, "url": f"/api/pessoas/{pessoaJuridica.id}"})
    pessoaTemporaria = ["nome", "endereco", "contato"]
    for i in pessoaTemporaria:
        if not(i in pessoa and pessoa[i]):
                abort(400, "Dados insuficientes")
        pessoaProjeto = Pessoa(pessoa["nome"], pessoa["endereco"], pessoa["contato"])
        pessoas.append(pessoaProjeto)
        return jsonify({"id": pessoaProjeto.id, "url": f"/api/pessoas/{pessoaProjeto.id}"})