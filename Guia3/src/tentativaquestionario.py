from typing import List, Tuple, Dict
from .perguntamultiplaescolha import PerguntaMultiplaEscolha
from .respostaobjetiva import RespostaObjetiva
from .respostadiscursiva import RespostaDiscursiva

class TentativaQuestionario:
    def __init__(self, questionario, usuario, data_inicio=None, data_fim=None):
        self.__questionario = questionario
        self.usuario = usuario
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.respostas = []
        self.__finalizado = False
    
    def registrar_resposta(self, indice_pergunta, valor):
        pergunta = self.__questionario.perguntas[indice_pergunta]

        if isinstance(pergunta, PerguntaMultiplaEscolha):
            resposta = RespostaObjetiva(pergunta=pergunta, indice_escolhido=valor)
        else:
            resposta = RespostaDiscursiva(pergunta=pergunta, texto_resposta=valor)

        self.respostas.append(resposta)
        return resposta

    def adicionar_pergunta(self, p):
        self.__questionario.adicionar_pergunta(p)

    def finalizar(self):
        self.__finalizado = True
        pontuacao = self.calcular_pontuacao()
        feedback = f"Pontuação final: {pontuacao}"
        return pontuacao, feedback

    def calcular_pontuacao(self):
        return sum(
            resposta.calcular_pontuacao()
            for resposta in self.respostas
        )
    
    def is_finalizado(self):
        return self.__finalizado

