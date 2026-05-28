from abc import ABC, abstractmethod
from typing import Optional, Any

class Pergunta(ABC):
    def __init__(self, texto: str, explicacao_geral: Optional[str] = None):
        self.texto: str = texto
        self.explicacao_geral: Optional[str] = explicacao_geral

    @abstractmethod
    def validar_resposta(self, resposta: Any) -> bool:
        pass

    def get_explicacao(self) -> str:
        return self.explicacao_geral if self.explicacao_geral is not None else ""

    @abstractmethod
    def get_tipo(self) -> str:
        pass