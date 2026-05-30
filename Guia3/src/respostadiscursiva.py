from typing import List, Tuple, Dict

class RespostaDiscursiva:
    def __init__(self, pergunta, texto_resposta):
        self.pergunta = pergunta
        self.texto_resposta = texto_resposta
    @property
    def esta_correta(self):
        return self.pergunta.validar_resposta(self.texto_resposta)
    
    def calcular_pontuacao(self):
        if self.esta_correta == True:
            return 1