from datetime import datetime
class ListaTarefa: 
    def __init__(self):
        self._tarefas = []
        self._quantidadeTarefas = 0
    def adicionaTarefa(self, tarefa):
        self._tarefas.append(tarefa)
        self._quantidadeTarefas += 1 
    def getTarefas(self, concluido=False):
        self.retornaTarefas = []
        for tarefa in self._tarefas:
            if concluido==True or tarefa.concluido==False:
                self.retornaTarefas.append(tarefa)
        return self.retornaTarefas
    def getQuantidadeTarefas(self):
        return self._quantidadeTarefas
    def getTarefasAtrasadas(self):
        self.retornaTarefas = []
        for tarefa in self._tarefas:
            if tarefa.concluido == False and datetime.now() > tarefa.dataPrevistaEntrega:
                self.retornaTarefas.append(tarefa)
        return self.retornaTarefas
    def getTarefasParaHoje(self):
        self.retornaTarefas = []
        for tarefa in self._tarefas:
            if tarefa.dataPrevistaEntrega.day == datetime.now().day:
                self.retornaTarefas.append(tarefa)
        return self.retornaTarefas