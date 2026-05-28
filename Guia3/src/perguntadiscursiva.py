from typing import List, Tuple, Dict
from pergunta import Pergunta

class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto, explicacao_geral, resposta_esperada=None):
        self.resposta_esperada = resposta_esperada
        super().__init__(texto, explicacao_geral)

    def validar_resposta(self, resposta) -> bool:
        if resposta.lower() == self.resposta_esperada.lower():
            return True
        else:
            return False

    def get_explicacao(self):
        return self.explicacao_geral

    def get_tipo(self) -> str:
        return "discursiva"