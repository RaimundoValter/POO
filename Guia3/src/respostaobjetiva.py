from typing import List, Tuple, Dict

class RespostaObjetiva:
    def __init__(self, pergunta, indice_escolhido: int):
        self.pergunta = pergunta
        self.indice_escolhido = indice_escolhido
        self.alternativa_selecionada = pergunta.alternativas[indice_escolhido]
        self.esta_correta = pergunta.validar_resposta(indice_escolhido)

    def calcular_pontuacao(self) -> float:
        return 1.0 if self.esta_correta else 0.0