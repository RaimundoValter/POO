from typing import List, Tuple, Dict

from Guia3.src.pergunta import Pergunta

class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto: str, explicacao_geral: str, resposta_certa: str):
        super().__init__(texto, explicacao_geral)
        self.resposta_certa = resposta_certa

    def validar_resposta(self, resposta: str) -> bool:
        return resposta == self.resposta_certa

    def get_explicacao(self) -> str:
        return self.explicacao_geral

    def get_tipo(self) -> str:
        return "Discursiva"
    
    