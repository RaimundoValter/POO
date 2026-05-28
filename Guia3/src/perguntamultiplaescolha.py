from typing import List, Tuple, Dict

class PerguntaMultiplaEscolha:
    def __init__(self, texto: str, alternativas: List[Tuple[str, bool]], explicacao_geral: str = ""):
        self.texto = texto
        self.alternativas = alternativas
        self.explicacao_geral = explicacao_geral

    def validar_resposta(self, resposta) -> bool:
        if isinstance(resposta, int):
            if 0 <= resposta < len(self.alternativas):
                return self.alternativas[resposta][1]
            return False

        if isinstance(resposta, str):
            for texto, correta in self.alternativas:
                if texto == resposta:
                    return correta
            return False

        if isinstance(resposta, (list, tuple, set)):
            selecionadas = set()
            for item in resposta:
                if isinstance(item, int):
                    if 0 <= item < len(self.alternativas):
                        selecionadas.add(self.alternativas[item][0])
                    else:
                        return False
                elif isinstance(item, str):
                    selecionadas.add(item)
                else:
                    return False

            corretas = {texto for texto, correta in self.alternativas if correta}
            return selecionadas == corretas

        return False

    def get_explicacao(self) -> str:
        return self.explicacao_geral

    def get_tipo(self) -> str:
        return "multipla_escolha"
