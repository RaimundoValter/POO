from typing import List, Tuple, Dict
from abc import ABC
from abc import abstractmethod

class Resposta(ABC):
    def __init__(self, pergunta, pontuacao_obtida, esta_correta=False):
        self._pergunta = pergunta
        self._pontuacao_obtida = pontuacao_obtida
        self._esta_correta = esta_correta
        
    @property
    def pergunta(self):
        return self._pergunta
    
    @property
    def esta_correta(self):
        return self._esta_correta
    
    @property
    def pontuacao_obtida(self):
        return self.pontuacao_obtida

    @abstractmethod    
    def calcular_pontuacao():
        pass