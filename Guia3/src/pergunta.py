from typing import List, Tuple, Dict
from abc import ABC, abstractmethod
class Pergunta(ABC):
    def __init__(self, texto, explicacao_geral=None):
        self.__texto = texto
        self.__explicacao_geral = explicacao_geral

    @abstractmethod
    def validar_resposta(self, resposta) -> bool:
        pass

    def get_explicacao(self):
        return self.__explicacao_geral
    
    @abstractmethod
    def get_tipo(self) -> str:
        pass