from typing import List, Tuple, Dict
from abc import ABC, abstractmethod

class Pergunta(ABC):
    def __init__(self, texto, explicacao_geral = None):
        self.texto = texto
        self.explicacao_geral = explicacao_geral

    def get_explicacao(self):
        return self.explicacao_geral

    @abstractmethod
    def validar_resposta(self, resposta):
        pass
    
    @abstractmethod
    def get_tipo(self):
        return self.get_tipo