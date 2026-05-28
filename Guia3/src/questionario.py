from typing import List, Tuple, Dict

class Questionario:
    def __init__(self, resposta_esperada=None, case_sensitive: bool = False):
        self.resposta_esperada = resposta_esperada
        self.case_sensitive = case_sensitive
        self.perguntas = []

    def adicionar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

    def validar_resposta(self, texto: str) -> bool:
        if self.resposta_esperada is None:
            return True
        if self.case_sensitive:
            return texto == self.resposta_esperada
        return texto.lower() == self.resposta_esperada.lower()  