from typing import List, Tuple, Dict
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha
from src.perguntadiscursiva import PerguntaDiscursiva
from src.respostaobjetiva import RespostaObjetiva
from src.respostadiscursiva import RespostaDiscursiva
from datetime import datetime

class TentativaQuestionario:
    def __init__(self, questionario, usuario):
        self.questionario = questionario
        self.usuario = usuario
        self.data_inicio = datetime.now()
        self.data_fim = None
        self.respostas = []

    def registrar_resposta(self, indice_pergunta, valor):
        pergunta = self.questionario.perguntas[
            indice_pergunta
        ]

        if isinstance(pergunta, PerguntaMultiplaEscolha):
            resposta = RespostaObjetiva(
                pergunta,
                valor
            )

        elif isinstance(pergunta, PerguntaDiscursiva):
            resposta = RespostaDiscursiva(
                pergunta,
                valor
            )

        else:
            raise TypeError("Tipo de pergunta inválido")

        self.respostas.append(resposta)

    def calcular_pontuacao(self):
        return sum(
            resposta.calcular_pontuacao()
            for resposta in self.respostas
        )

    def finalizar(self):
        self.data_fim = datetime.now()

        pontuacao = self.calcular_pontuacao()

        feedback = (
            f"Usuário {self.usuario} finalizou o quiz "
            f"com {pontuacao} ponto(s)."
        )

        return pontuacao, feedback

    def is_finalizado(self):
        return self.data_fim is not None