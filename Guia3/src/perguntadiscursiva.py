from typing import List, Tuple, Dict
from pergunta import Pergunta

class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto, explicacao_geral = None, resposta_esperada: str = None):
        super().__init__(texto, explicacao_geral)
        self.resposta_esperada = resposta_esperada

    def validar_resposta(self, texto: str):
        if self.resposta_esperada is None:
            return False
        return texto.strip().lower() == self.resposta_esperada.strip().lower()
    
    def get_explicacao(self) -> str:
        return self.explicacao_geral
    
    def get_tipo(self):
        return "discursiva"