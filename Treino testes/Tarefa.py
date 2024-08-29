from datetime import datetime
class Tarefa:
    def __init__(self, nome, descricao="", notificacao=None, dataPrevistaEntrega=None, concluido=False):
        self.nome = nome
        self.descricao = descricao
        self.notificacao = notificacao
        self.dataPrevistaEntrega = dataPrevistaEntrega
        self.concluido = concluido
    def setDescricao(self, descricao):
        self.descricao = descricao
    def setNotificacao(self, notificacao):
        self.notificacao = notificacao
    def setDataPrevistaEntrega(self, dataPrevistaEntrega):
        self.dataPrevistaEntrega = dataPrevistaEntrega
    def setConcluido(self, concluido):
        self.concluido = concluido
    def verificaAtraso(self):
        if datetime.now() > self.dataPrevistaEntrega:
            return True