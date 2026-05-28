from typing import List
from src.pergunta import Pergunta
from src.tentativaquestionario import TentativaQuestionario

class Questionario:
    def __init__(self, titulo: str):
        self.titulo: str = titulo
        self.perguntas: List[Pergunta] = []

    def adicionar_pergunta(self, p: Pergunta) -> None:
        self.perguntas.append(p)

    def criar_attempt(self, usuario: str) -> TentativaQuestionario:
        return TentativaQuestionario(self, usuario)

Quiz = Questionario