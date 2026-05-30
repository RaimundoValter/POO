from typing import List, Tuple, Dict
from pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto: str, alternativas: List[Tuple[str, bool]], explicacao_geral = None):
        super().__init__(texto, explicacao_geral)
        self.alternativas = alternativas
        self.explicacao_geral = explicacao_geral

    def _obter_texto_correta(self, alternativa):
        if isinstance(alternativa, tuple):
            return alternativa[0], alternativa[1]
        if isinstance(alternativa, dict):
            return alternativa.get("texto"), alternativa.get("correta", False)
        if hasattr(alternativa, "texto") and hasattr(alternativa, "correta"):
            return alternativa.texto, alternativa.correta
        return None, False

    def validar_resposta(self, resposta) -> bool:
        if isinstance(resposta, int):
            if 0 <= resposta < len(self.alternativas):
                _, correta = self._obter_texto_correta(self.alternativas[resposta])
                return correta
            return False

        if isinstance(resposta, str):
            for alternativa in self.alternativas:
                texto, correta = self._obter_texto_correta(alternativa)
                if texto == resposta:
                    return correta
            return False

        if isinstance(resposta, (list, tuple, set)):
            selecionadas = set()
            for item in resposta:
                if isinstance(item, int):
                    if 0 <= item < len(self.alternativas):
                        texto, _ = self._obter_texto_correta(self.alternativas[item])
                        selecionadas.add(texto)
                    else:
                        return False
                elif isinstance(item, str):
                    selecionadas.add(item)
                else:
                    return False

            corretas = {texto for alternativa in self.alternativas if (texto := self._obter_texto_correta(alternativa)[0]) is not None and self._obter_texto_correta(alternativa)[1]}
            return selecionadas == corretas

        return False

    def get_alternativa_correta(self):
        for alt in self.alternativas:
            _, correta = self._obter_texto_correta(alt)
            if correta:
                return alt
        return None
    
    def get_explicacao(self) -> str:
        return self.explicacao_geral

    def get_tipo(self) -> str:
        return "multipla_escolha"
