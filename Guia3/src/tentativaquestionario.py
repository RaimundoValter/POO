from typing import List, Tuple, Dict

class TentativaQuestionario:
    def __init__(self, questionario, usuario, data_inicio=None, data_fim=None):
        perguntas = []
        self.__questionario = questionario
        self.__usuario = usuario
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        respostas = []
    
    def registrar_resposta(self, indice_pergunta, valor):
        pass

    def adicionar_pergunta(self, p):
        self.perguntas.append(p)

    def finalizar():
        pass

    def calcular_pontuacao():
        pass
    
    def is_finalizado():
        pass

