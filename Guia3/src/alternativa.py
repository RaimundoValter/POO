from typing import List, Tuple, Dict

class Alternativa:
    def __init__(self, texto, correta, explicacao=None):
        self._texto = texto
        self._correta = correta
        self._explicacao = explicacao
        
    @property
    def texto(self):
        return self._texto
    
    @property
    def correta(self):
        return self._correta
    
    @property
    def explicacao(self):
        return self._explicacao