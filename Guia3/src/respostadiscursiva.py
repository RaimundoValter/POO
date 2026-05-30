from typing import List, Tuple, Dict
from src.pergunta import Pergunta

class RespostaDiscursiva:
    def __init__(self, pergunta, texto_resposta: str):
        self.pergunta = pergunta
        self.texto_resposta = texto_resposta
        self.esta_correta = pergunta.validar_resposta(texto_resposta)

    def calcular_pontuacao(self) -> float:
        return 1.0 if self.esta_correta else 0.0