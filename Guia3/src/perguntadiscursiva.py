from typing import List, Tuple, Dict

class PerguntaDiscursiva:
    def __init__(self, texto, resposta_esperada=None, case_sensitive: bool = False):
        self.texto = texto
        self.resposta_esperada = resposta_esperada
        self.case_sensitive = case_sensitive

    def get_tipo(self):
        return "discursiva"

    def validar_resposta(self, texto: str):
        if self.resposta_esperada is None:
            return False
        if self.case_sensitive:
            return texto == self.resposta_esperada
        return texto.strip().lower() == self.resposta_esperada.strip().lower()