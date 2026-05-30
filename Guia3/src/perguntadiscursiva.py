from typing import List, Tuple, Dict
from .pergunta import Pergunta

class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto, explicacao_geral=None, resposta_esperada=None):
        super().__init__(texto, explicacao_geral)
        self.resposta_esperada = resposta_esperada

    def validar_resposta(self, resposta) -> bool:
        if self.resposta_esperada is None or resposta is None:
            return False

        return resposta.lower() == self.resposta_esperada.lower()

    def get_tipo(self) -> str:
        return "discursiva"
    
    
    

    
