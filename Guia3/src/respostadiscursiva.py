from src.resposta import Resposta
from src.perguntadiscursiva import PerguntaDiscursiva

class RespostaDiscursiva(Resposta):
    def __init__(self, pergunta: PerguntaDiscursiva, texto_resposta: str):
        super().__init__(pergunta)
        self.texto_resposta: str = texto_resposta
        self.esta_correta = pergunta.validar_resposta(texto_resposta)

    def calcular_pontuacao(self) -> float:
        self.pontuacao_obtida = 1.0 if self.esta_correta else 0.0
        return self.pontuacao_obtida