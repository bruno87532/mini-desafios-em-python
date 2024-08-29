import unittest
from ListaTarefa import ListaTarefa
from Tarefa import Tarefa
from datetime import datetime, timedelta
class TestListaTarefa(unittest.TestCase):
    def setUp(self):
        self.listaTarefa = ListaTarefa()
        self.tarefa = Tarefa("Curso de Python")
        self.tarefa2 = Tarefa("Curso de Python", concluido=True)
    def testInserindoUmaTarefaNaLista(self):
        self.listaTarefa.adicionaTarefa(self.tarefa)
        self.assertIn(self.tarefa, self.listaTarefa.getTarefas())
    def testVerificandoSeGetTarefasRetornaTarefasConcluidasENaoConcluidasSeGetTarefasParametroCondluidoETrue(self):
        self.listaTarefa.adicionaTarefa(self.tarefa)
        self.listaTarefa.adicionaTarefa(self.tarefa2)
        self.assertIn(self.tarefa, self.listaTarefa.getTarefas(concluido=True))
        self.assertIn(self.tarefa2, self.listaTarefa.getTarefas(concluido=True))
    def testVerificandoSeGetTarefasRetornaApenasTarefasNaoConcluidasSeGetTarefasParametroCondluidoEFalse(self):
        self.listaTarefa.adicionaTarefa(self.tarefa)
        self.listaTarefa.adicionaTarefa(self.tarefa2)
        self.assertIn(self.tarefa, self.listaTarefa.getTarefas()) # O Método getTarefas por padrão já tem o parâmetro concluido = False, por isso não preciso passar
        self.assertNotIn(self.tarefa2, self.listaTarefa.getTarefas())
    def testVerificaSeGetQuantidadeTarefasRetornaAQuantidadeCerta(self):
        self.listaTarefa.adicionaTarefa(self.tarefa)
        self.assertEqual(1, self.listaTarefa.getQuantidadeTarefas())
        self.listaTarefa.adicionaTarefa(self.tarefa2)
        self.assertEqual(2, self.listaTarefa.getQuantidadeTarefas())
    def testVerificaSeGetTarefasParaHojeRetornaTarefasApenasParaODiaDeHoje(self):
        self.tarefa.setDataPrevistaEntrega(datetime.now())
        self.tarefa2.setDataPrevistaEntrega(datetime.now() + timedelta(days=1))
        self.listaTarefa.adicionaTarefa(self.tarefa)
        self.listaTarefa.adicionaTarefa(self.tarefa2)
        self.assertIn(self.tarefa, self.listaTarefa.getTarefasParaHoje())
        self.assertNotIn(self.tarefa2, self.listaTarefa.getTarefasParaHoje())
    def testVerificaSeGetTarefasAtrasadasRetornaApenasTarefasAtrasadas(self):
        self.tarefa.setDataPrevistaEntrega(datetime(2024, 8, 20, 16))
        self.tarefa2.setDataPrevistaEntrega(datetime.now() + timedelta(days=1))
        self.listaTarefa.adicionaTarefa(self.tarefa)
        self.listaTarefa.adicionaTarefa(self.tarefa2)
        self.assertIn(self.tarefa, self.listaTarefa.getTarefasAtrasadas())
        self.assertNotIn(self.tarefa2, self.listaTarefa.getTarefasAtrasadas())
unittest.main()