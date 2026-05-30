from typing import List, Tuple, Dict
from pergunta import Pergunta
from abc import ABC

class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto, explicacao_geral=None, resposta_esperada=None, case_sensitive=False):
        super().__init__(texto, explicacao_geral)
        self._resposta_esperada = resposta_esperada
        self._case_sensitive = case_sensitive

    @property
    def resposta_esperada(self):
        return self._resposta_esperada
    
    @property
    def case_sensitive(self):
        return self._case_sensitive

    def validar_resposta(self, texto):
        if self.resposta_esperada is None:
            return False

        if self.case_sensitive:
            return texto == self.resposta_esperada

        return texto.strip().lower() == \
            self.resposta_esperada.strip().lower()

    def get_tipo(self):
        return "discursiva"