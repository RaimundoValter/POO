from datetime import datetime
from typing import List, Optional, Tuple, Any
from src.resposta import Resposta
from src.respostaobjetiva import RespostaObjetiva
from src.respostadiscursiva import RespostaDiscursiva
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha
from src.perguntadiscursiva import PerguntaDiscursiva

class TentativaQuestionario:
    def __init__(self, questionario, usuario: str):
        self.questionario = questionario
        self.usuario: str = usuario
        self.data_inicio: Optional[datetime] = datetime.now()
        self.data_fim: Optional[datetime] = None
        self.respostas: List[Optional[Resposta]] = [None] * len(questionario.perguntas)

    def registrar_resposta(self, indice_pergunta: int, valor: Any) -> None:
        if self.is_finalizado():
            raise ValueError("A tentativa já foi finalizada.")
            
        if not (0 <= indice_pergunta < len(self.questionario.perguntas)):
            raise IndexError("Índice de pergunta inválido.")

        pergunta = self.questionario.perguntas[indice_pergunta]

        if isinstance(pergunta, PerguntaMultiplaEscolha) and isinstance(valor, int):
            self.respostas[indice_pergunta] = RespostaObjetiva(pergunta, valor)
        elif isinstance(pergunta, PerguntaDiscursiva) and isinstance(valor, str):
            self.respostas[indice_pergunta] = RespostaDiscursiva(pergunta, valor)
        else:
            raise TypeError("O tipo de resposta é incompatível com a pergunta.")

    def calcular_pontuacao(self) -> float:
        pontuacao_total = 0.0
        for resposta in self.respostas:
            if resposta is not None:
                pontuacao_total += resposta.calcular_pontuacao()
        return pontuacao_total

    def is_finalizado(self) -> bool:
        return self.data_fim is not None

    def finalizar(self) -> Tuple[float, str]:
        if not self.is_finalizado():
            self.data_fim = datetime.now()
        
        pontuacao = self.calcular_pontuacao()
        resumo = f"Tentativa concluída por {self.usuario}."
        return pontuacao, resumo

QuizAttempt = TentativaQuestionario