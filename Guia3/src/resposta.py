from typing import List, Tuple, Dict
from abc import ABC, abstractmethod
class Resposta(ABC):
    def __init__(self, pergunta: str,esta_correta: bool,pontuacao_obtida: int):
        self.pergunta = pergunta
        self.esta_correta = esta_correta
        self.pontuacao_obtida = pontuacao_obtida


    @abstractmethod
    def calcular_pontuacao(self) -> int:
        pass