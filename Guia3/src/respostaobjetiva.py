from typing import List, Tuple, Dict
from .resposta import Resposta
class RespostaObjetiva(Resposta):
    def __init__(self, pergunta, indice_escolhido, pontuacao_obtida=None):
        self.indice_escolhido = indice_escolhido
        esta_correta = pergunta.validar_resposta(indice_escolhido)
        super().__init__(pergunta, esta_correta, pontuacao_obtida)

    def calcular_pontuacao(self):
        if self.esta_correta:
            return 1.0
        else:
            return 0.0

        