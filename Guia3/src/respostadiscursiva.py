from typing import List, Tuple, Dict
from .resposta import Resposta

class RespostaDiscursiva(Resposta):
    def __init__(self, pergunta, texto_resposta, pontuacao_obtida=None):
        self.texto_resposta = texto_resposta
        esta_correta = pergunta.validar_resposta(texto_resposta)
        super().__init__(pergunta, esta_correta, pontuacao_obtida)

    def calcular_pontuacao(self):
        if self.esta_correta:
            return 1.0
        else:
            return 0.0   