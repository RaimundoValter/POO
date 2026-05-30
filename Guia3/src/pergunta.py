from typing import List, Tuple, Dict
from abc import ABC, abstractmethod

class Pergunta(ABC):
    def __init__(self, texto, explicacao_geral=None):
        self._texto = texto
        self._explicacao_geral = explicacao_geral

    @property
    def texto(self):
        return self._texto
    
    @property
    def respostas(self):
        return self._respostas
    
    @property
    def explicacao_geral(self):
        return self._explicacao_geral
        
    @abstractmethod
    def validar_resposta(self, resposta):
        pass

    @abstractmethod
    def get_tipo(self):
        pass

    def get_explicacao(self):
        return self.explicacao_geral