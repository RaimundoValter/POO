from typing import List
from src.tentativaquestionario import TentativaQuestionario

class Questionario:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.perguntas: List = []

    def adicionar_pergunta(self, pergunta) -> None:
        self.perguntas.append(pergunta)

    def criar_attempt(self, usuario: str):
        return TentativaQuestionario(questionario = self, usuario = usuario)