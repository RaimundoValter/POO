from typing import List, Tuple, Dict

class RespostaObjetiva:
    def __init__(self, pergunta, indice_escolhido):
        self.pergunta = pergunta
        self.indiece_escolhido = indice_escolhido
    
    @property
    def esta_correta(self):
        return self.pergunta.validar_resposta(self.indiece_escolhido)
    
    def calcular_pontuacao(self):
        if self.esta_correta == True:
            return 1
        else:
            return 0
    
