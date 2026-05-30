from typing import List, Tuple, Dict
from pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto, alternativas, explicacao_geral = None):
        super().__init__(texto, explicacao_geral)
        self.alternativas = alternativas

    def validar_resposta(self, indice):
        return self.alternativas[indice].correta

    def get_alternativa_correta(self):
        for alternativa in self.alternativas:
            if alternativa.correta:
                return alternativa
        return None
    
    def get_tipo(self):
        return "multipla_escolha"