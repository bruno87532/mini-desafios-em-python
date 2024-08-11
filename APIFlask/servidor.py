from flask import Flask

servidor = Flask(__name__)

@servidor.route("/")
def helloWorld():
    return "Hello World"
