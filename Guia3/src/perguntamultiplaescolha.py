from typing import List, Tuple, Dict
from .pergunta import Pergunta
from .alternativa import Alternativa

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto, alternativas, explicacao_geral=None):
        super().__init__(texto, explicacao_geral)
        self.alternativas = alternativas or []
    
    def validar_resposta(self, indice: int) -> bool:
        if indice is None or indice < 0 or indice >= len(self.alternativas):
            return False

        return self.alternativas[indice] == self.get_alternativa_correta()

    def get_alternativa_correta(self) -> Alternativa:
        for alternativa in self.alternativas:
            if alternativa.correta == True:
                return alternativa
        return None

    def get_tipo(self) -> str:
        return "multipla_escolha"
    
    
    
