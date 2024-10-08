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
    pessoa = Pessoa.localizaPessoa(id, pessoas)
    return jsonify(pessoa.__dict__)
@servidor.route("/api/pessoas/", methods=["POST"])
def adicionaPessoa():
    if not request.data:
        abort(400, "Dados insuficientes")
    pessoa = request.get_json()
    if "cpf" in pessoa:
        tipoPessoa = PessoaFisica
    elif "cnpj" in pessoa:
        tipoPessoa = PessoaJuridica
    else:
        tipoPessoa = Pessoa
    novaPessoa = tipoPessoa.adicionaPessoa(pessoa)
    pessoas.append(novaPessoa)
    return jsonify({"id": novaPessoa.id, "url": f"/api/pessoas/{novaPessoa.id}/"})
@servidor.route("/api/pessoas/<int:id>", methods=["POST"])
def deletaPessoa(id):
    pessoa = Pessoa.localizaPessoa(id, pessoas)
    pessoas.remove(pessoa)
@servidor.route("/api/pessoas/<int:id>", methods=["PUT"])
def editaPessoa(id):
    if not request.data:
        abort(400, "Dados insuficientes")
    dados = request.get_json()
    pessoa = Pessoa.localizaPessoa(id, pessoas)
    pessoa.editaPessoa(dados)
    return jsonify(pessoa.__dict__)
@servidor.route("/api/pessoas/<int:id>", methods=["PATCH"])
def editaPessoaParcial(id):
    if not request.data:
        abort(400, "Dados insuficientes")
    dados = request.get_json()
    pessoa = Pessoa.localizaPessoa(id, pessoas)
    pessoa.editaPessoaParcial(dados)
    return jsonify(pessoa.__dict__)