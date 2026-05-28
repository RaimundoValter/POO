from typing import List, Tuple, Dict
from pergunta import Pergunta     

class PerguntaDiscursiva(Pergunta):
    def __init__(self, resposta_esperada, case_sensitive):
        self.resposta_esperada = resposta_esperada
        self.case_sensitive = case_sensitive
    
    def validar_resposta(self,texto):
        if texto == self.resposta_esperada:
            return 1
        return 0
    