from typing import List, Tuple, Dict
from tentativaquestionario import TentativaQuestionario
class Questionario:
    def __init__(self, titulo: str):
        perguntas = []
        self.__titulo = titulo
        
    def registrar_resposta(self, indice_pergunta, valor):
        pass

    def adicionar_pergunta(self, p):
        self.perguntas.append(p)

    def criar_attempt(self, usuario):
        tentativa = TentativaQuestionario(self, usuario)


    def finalizar():
        pass
    def calcular_pontuacao():
        pass
    def is_finalizado():
        pass

