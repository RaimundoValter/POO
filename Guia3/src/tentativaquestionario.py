from typing import List, Tuple
from datetime import datetime
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha
from src.respostaobjetiva import RespostaObjetiva
from src.respostadiscursiva import RespostaDiscursiva

class TentativaQuestionario:
    def __init__(self, questionario, usuario: str):
        self.questionario = questionario
        self.usuario = usuario
        self.data_inicio = datetime.now()
        self.data_fim = None
        self.respostas: List = []
        self._finalizado: bool = False

    def registrar_resposta(self, indice_pergunta: int, valor) -> None:
        pergunta = self.questionario.perguntas[indice_pergunta]

        if isinstance(pergunta, PerguntaMultiplaEscolha):
            resposta = RespostaObjetiva(pergunta = pergunta, indice_escolhido=valor)
        else:
            resposta = RespostaDiscursiva(pergunta = pergunta, texto_resposta=valor)

        self.respostas.append(resposta)

    def calcular_pontuacao(self) -> float:
        return sum(r.calcular_pontuacao() for r in self.respostas)

    def finalizar(self) -> Tuple[float, str]:
        self._finalizado = True
        self.data_fim = datetime.now()
        pontuacao = self.calcular_pontuacao()
        total = len(self.questionario.perguntas)
        feedback = f"Você acertou {pontuacao:.0f} de {total} perguntas."
        return pontuacao, feedback

    def is_finalizado(self) -> bool:
        return self._finalizado