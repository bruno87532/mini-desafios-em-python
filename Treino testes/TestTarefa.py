import unittest
from datetime import datetime, timedelta
from Tarefa import Tarefa
class TestTarefa(unittest.TestCase):
    def setUp(self):
        self.tarefa = Tarefa("Curso de Python")
    def testCriaTarefaApenasComONome(self):
        self.assertEqual(self.tarefa.nome, "Curso de Python")
    def testCriaTarefaComTodosOsAtributos(self):
        self.tarefa = Tarefa("Curso de Python", "Estou fazendo um curso de Python", datetime(2024, 9, 25, 16), datetime(2024, 9, 29, 16), True)
        self.assertEqual(self.tarefa.nome, "Curso de Python")
        self.assertEqual(self.tarefa.descricao, "Estou fazendo um curso de Python")
        self.assertEqual(self.tarefa.notificacao, datetime(2024, 9, 25, 16))
        self.assertEqual(self.tarefa.dataPrevistaEntrega, datetime(2024, 9, 29, 16))
        self.assertEqual(self.tarefa.concluido, True)
    def testInserindoAtributoDescricaoEmUmaTarefaJaCriada(self):
        self.tarefa.setDescricao("Estou fazendo um curso de Python")
        self.assertEqual(self.tarefa.descricao, "Estou fazendo um curso de Python")
    def testInserindoAtributoNotificacaoEmUmaTarefaJaCriada(self):
        self.tarefa.setNotificacao(datetime(2024, 9, 25, 16))
        self.assertEqual(self.tarefa.notificacao, datetime(2024, 9, 25, 16))
    def testInserindoAtributoDataPrevistaEntregaEmUmaTarefaJaCriada(self):
        self.tarefa.setNotificacao(datetime(2024, 9, 29, 16))
        self.assertEqual(self.tarefa.notificacao, datetime(2024, 9, 29, 16))
    def testInserindoAtributoConcluidoEmUmaTarefaJaCriada(self):
        self.tarefa.setConcluido(True)
        self.assertEqual(self.tarefa.concluido, True)
    def testVerificaSeInsereTrueNoAtributoConcluidoDeUmaTarefaConcluidaMantemTrue(self):
        self.tarefa.setConcluido(True)
        self.assertEqual(self.tarefa.concluido, True)
        self.tarefa.setConcluido(True)
        self.assertEqual(self.tarefa.concluido, True)
    def testVerificandoSeVerificaAtrasoRetornaTrueParaSeDataAtualMaiorQueDataPrevistaEntrega(self):
        self.tarefa.setDataPrevistaEntrega(datetime(2024, 8, 20, 16))
        self.assertEqual(True, datetime.now() > self.tarefa.dataPrevistaEntrega)
    def testVerificandoSeVerificaAtrasoRetornaFalseeParaSeDataAtualMenorQueDataPrevistaEntrega(self):
        self.tarefa.setDataPrevistaEntrega(datetime.now() + timedelta(days=1))
        self.assertEqual(True, datetime.now() < self.tarefa.dataPrevistaEntrega)            
unittest.main()