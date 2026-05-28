from typing import Optional
from src.pergunta import Pergunta

class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto: str, resposta_esperada: Optional[str] = None, case_sensitive: bool = False, explicacao_geral: Optional[str] = None):
        super().__init__(texto, explicacao_geral)
        self.resposta_esperada: Optional[str] = resposta_esperada
        self.case_sensitive: bool = case_sensitive

    def validar_resposta(self, texto: str) -> bool:
        if self.resposta_esperada is None:
            return True
        
        if not self.case_sensitive:
            return texto.strip().lower() == self.resposta_esperada.strip().lower()
        
        return texto.strip() == self.resposta_esperada.strip()

    def get_tipo(self) -> str:
        return "discursiva"