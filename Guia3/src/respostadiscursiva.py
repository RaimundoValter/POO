from typing import List, Tuple, Dict
from resposta import Resposta

class RespostaDiscursiva(Resposta):
    def __init__(self, pergunta, esta_correta, texto_resposta):
        super().__init__(pergunta, esta_correta)
        self._texto_resposta = texto_resposta

    @property
    def texto_resposta(self):
        return self._texto_resposta
    
    def calcular_pontuacao(self):
      return 1.0 if self.esta_correta else 0.0
