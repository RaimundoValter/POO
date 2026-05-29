from typing import List, Tuple, Dict

from Guia3.src.pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto: str, explicacao_geral: str, alternativas: List[Dict[str, str]]):
        super().__init__(texto, explicacao_geral)
        self.alternativas = alternativas

    def validar_resposta(self, resposta: str) -> bool:
        for alternativa in self.alternativas:
            if alternativa['texto'] == resposta:
                return alternativa['correta']
        return False

    def get_explicacao(self) -> str:
        return self.explicacao_geral

    def get_tipo(self) -> str:
        return "Multipla Escolha"