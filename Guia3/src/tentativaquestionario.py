from typing import List, Tuple, Dict

class TentativaQuestionario:
    def __init__(self, quiz, usuario):
        self.quiz = quiz
        self.usuario = usuario
        self.respostas = []
    
    
    @usuario.setter
    def usuario(self, novo_usuario):
        self.usuario = novo_usuario
    
    def registrar_resposta(self, indice, resposta):
        registro = [indice, resposta]
        self.respostas.append(registro)

    def calcular_pontuacao(self):
        pontuacao = 0
        for res in self.respostas:
            pergunta = self.quiz.perguntas[res[0]]

            if pergunta.validar_resposta(res[1]) == True:
                pontuacao = pontuacao +1
        return pontuacao
            