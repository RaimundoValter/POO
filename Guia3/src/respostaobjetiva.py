from typing import Optional
from src.resposta import Resposta
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha
from src.alternativa import Alternativa

class RespostaObjetiva(Resposta):
    def __init__(self, pergunta: PerguntaMultiplaEscolha, indice_escolhido: int):
        super().__init__(pergunta)
        self.indice_escolhido: int = indice_escolhido
        
        if 0 <= indice_escolhido < len(pergunta.alternativas):
            self.alternativa_selecionada: Optional[Alternativa] = pergunta.alternativas[indice_escolhido]
        else:
            self.alternativa_selecionada = None
            
        self.esta_correta = pergunta.validar_resposta(indice_escolhido)

    def calcular_pontuacao(self) -> float:
        self.pontuacao_obtida = 1.0 if self.esta_correta else 0.0
        return self.pontuacao_obtida