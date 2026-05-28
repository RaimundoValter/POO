from abc import ABC, abstractmethod
from src.pergunta import Pergunta

class Resposta(ABC):
    def __init__(self, pergunta: Pergunta):
        self.pergunta: Pergunta = pergunta
        self.esta_correta: bool = False
        self.pontuacao_obtida: float = 0.0

    @abstractmethod
    def calcular_pontuacao(self) -> float:
        pass