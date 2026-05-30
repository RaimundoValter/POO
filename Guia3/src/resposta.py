from typing import List, Tuple, Dict
from abc import ABC, abstractmethod

class Resposta(ABC):
    def __init__(self, pergunta):
        if type(self) is Resposta:
            raise TypeError(f'Não é permitido instanciar a classe abstrata Resposta  diretamente.')
        
        self.pergunta = pergunta 
        self.esta_correta = False
        self.pontuacao_obtida = 0.0

    @abstractmethod
    def calcular_pontuacao(self):
        pass