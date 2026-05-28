from typing import List, Tuple, Dict
from resposta import Resposta
class RespostaObjetiva(Resposta):
    def __init__(self, pergunta, esta_correta, pontuacao_obtida, indice_escolhido, alternativa_selecionada):
        self.__indice_escolhido = indice_escolhido
        self.alternativa_selecionada = alternativa_selecionada
        super().__init__(pergunta, esta_correta, pontuacao_obtida)

        