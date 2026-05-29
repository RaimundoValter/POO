from typing import List, Tuple, Dict

from Guia3.src.resposta import Resposta

class RespostaObjetiva(Resposta):
    def __init__(self, pergunta: str, esta_correta: bool, pontuacao_obtida: int):
        super().__init__(pergunta, esta_correta, pontuacao_obtida)

    def calcular_pontuacao(self) -> int:
        return self.pontuacao_obtida
    
    