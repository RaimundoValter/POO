from typing import List, Tuple, Dict
from abc import ABC, abstractmethod

class Pergunta(ABC):
    def __init__(self, texto: str, explicacao_geral: str):
        self.texto = texto
        self.explicacao_geral = explicacao_geral

    @abstractmethod
    def validarr_resposta(self, resposta: str) -> bool:
        pass

    @abstractmethod
    def get_explicacao(self) -> str:
        pass

    @abstractmethod
    def get_tipo(self) -> str:
        pass