from abc import ABC
from typing import List, Tuple, Dict

class Resposta(ABC):
    def __init__(self,pergunta, esta_correta: bool, pontuacao_obtida: float):
        self.pergunta = pergunta
        self.esta_correta = esta_correta
        self.pontuacao_obtida = pontuacao_obtida
    
    def calcular_pontuacao(self):
        pass