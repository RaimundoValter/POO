from typing import List, Tuple, Dict
from abc import ABC, abstractMethod
class Pergunta(ABC):
    def __init__(self, texto, explicacao_geral=None):
        self.__texto = texto
        self.__explicacao_geral = explicacao_geral

    def validarResposta(resposta) -> bool:
        pass

    def get_explicacao(self):
        return self.explicacao_geral

    def get_tipo() -> str:
        pass