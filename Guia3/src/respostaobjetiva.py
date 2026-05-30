from typing import List, Tuple, Dict
from abc import ABC
from resposta import Resposta

class RespostaObjetiva(Resposta):
    def __init__(self, pergunta, esta_correta, pontuacao_obtida, indice_escolhido, alternativa_selecionada=None):
        super().__init__(pergunta, esta_correta, pontuacao_obtida)
        self._indice_escolhido = indice_escolhido
        self._alternativa_selecionada = alternativa_selecionada
        
        if 0 <= indice_escolhido < len(pergunta.alternativas):
            self.alternativa_selecionada = \
                pergunta.alternativas[indice_escolhido]
        else:
            self.alternativa_selecionada = None

        self.esta_correta = pergunta.validar_resposta(
            indice_escolhido
        )

        self.pontuacao_obtida = self.calcular_pontuacao()
        
    @property
    def indice_escolhido(self):
        return self._indice_escolhido
    
    @property
    def alternativa_selecionada(self):
        return self._alternativa_selecionada

    def calcular_pontuacao(self):
      #  return 1.0 if self.esta_correta else 0.0
      if self.esta_correta:
        return 1
      else:
         return 0 
    
