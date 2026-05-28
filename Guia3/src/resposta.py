from typing import List, Tuple, Dict
from pergunta import Pergunta
from abc import ABC, abstractmethod
class Resposta(ABC):
    def __init__(self, pergunta: Pergunta, esta_correta, pontuacao_obtida):
        self.__pergunta = pergunta
        self.esta_correta = esta_correta
        self.pontuacao_obtida = pontuacao_obtida

    def calcular_pontuacao() -> float:
        pass

        