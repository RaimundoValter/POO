from typing import List, Tuple, Dict
from resposta import Resposta

class RespostaObjetiva(Resposta):
    def __init__(self, pergunta, indice_escolhido):
        super().__init__(pergunta)
        self.indice_escolhido = indice_escolhido
        self.esta_correta = pergunta.validar_resposta(indice_escolhido)
        self.alternativa_selecionada = pergunta.alternativas[indice_escolhido]

    def calcular_pontuacao(self):
        if self.esta_correta:
            self.pontuacao_obtida = 1.0
        else:
            self.pontuacao_obtida = 0.0

        return self.pontuacao_obtida

        