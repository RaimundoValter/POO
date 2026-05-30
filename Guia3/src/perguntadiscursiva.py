from typing import List, Tuple, Dict
from pergunta import Pergunta


class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto, resposta_esperada = None, case_sensitive = False):
        super().__init__(texto)
        self.resposta_esperada = resposta_esperada
        self.case_sensitive = case_sensitive

    def validar_resposta(self, texto):
        if self.resposta_esperada is None:
            return False
        
        resp_usuario = texto.strip()
        resp_esperada = self.resposta_esperada.strip()

        if not self.case_sensitive:
            return resp_usuario.lower() == resp_esperada.lower()
        
        return resp_usuario == resp_esperada
    
    def get_tipo(self):
        return "discursiva"
