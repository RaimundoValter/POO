from typing import List, Optional
from src.pergunta import Pergunta
from src.alternativa import Alternativa

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto: str, alternativas: List[Alternativa], explicacao_geral: Optional[str] = None):
        super().__init__(texto, explicacao_geral)
        if len(alternativas) < 2:
            raise ValueError("ERRO. A pergunta de multipla escolha deve ter no minimo duas alternativas")
        self.alternativas: List[Alternativa] = alternativas

    def validar_resposta(self, indice: int) -> bool:
        if 0 <= indice < len(self.alternativas):
            return self.alternativas[indice].correta
        return False

    def get_alternativa_correta(self) -> Alternativa:
        for alt in self.alternativas:
            if alt.correta:
                return alt
        raise ValueError("Nenhuma alternativa correta foi definida.")

    def get_tipo(self) -> str:
        return "multipla_escolha"