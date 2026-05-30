from typing import List, Tuple, Dict
from resposta import Resposta

class RespostaDiscursiva(Resposta):
    def __init__(self, pergunta, texto_resposta):
        super().__init__(pergunta)
        self.texto_resposta = texto_resposta
        self.esta_correta = pergunta.validar_resposta(texto_resposta)

    def calcular_pontuacao(self):
        if self.esta_correta:
            self.pontuacao_obtida = 1.0
        else:
            self.pontuacao_obtida = 0.0

        return self.pontuacao_obtida