from typing import List, Tuple, Dict
from pergunta import Pergunta
from alternativa import Alternativa

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, pergunta, texto, explicacao_geral):
        self.pergunta = pergunta
        self.alternativas = []
        super().__init__(texto, explicacao_geral)
    
    def validar_resposta(indice: int) -> bool:
        pass

    def get_alternativa_correta(self) -> Alternativa:
        for alternativa in self.alternativas:
            if alternativa.correta == True:
                return alternativa

    def validarResposta(self, resposta) -> bool:
        if resposta.lower() == self.resposta_esperada.lower():
            return True
        else:
            return False

    def get_explicacao(self):
        return self.explicacao_geral

    def get_tipo() -> str:
        return "multipla_escolha"
