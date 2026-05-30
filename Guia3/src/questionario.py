from typing import List, Tuple, Dict
from abc import ABC

from src.tentativaquestionario import TentativaQuestionario

class Questionario:
    def __init__(self, titulo):
        self._titulo = titulo
        self._perguntas = []

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def perguntas(self):
        return self._perguntas
        
    def adicionar_pergunta(self, pergunta):
        self._perguntas.append(pergunta)

    def criar_attempt(self, usuario):
        return TentativaQuestionario(self, usuario)