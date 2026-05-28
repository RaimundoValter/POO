from typing import Optional

class Alternativa:
    def __init__(self, texto: str, correta: bool, explicacao: Optional[str] = None):
        self.texto: str = texto
        self.correta: bool = correta
        self.explicacao: Optional[str] = explicacao