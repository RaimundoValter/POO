from datetime import datetime
from src.respostadiscursiva import RespostaDiscursiva
from src.respostaobjetiva import RespostaObjetiva

class TentativaQuestionario:
    def __init__(self, questionario, usuario):
        self.questionario = questionario  
        self.usuario = usuario            
        self.respostas = []               
        self.data_inicio = datetime.now()
        self.data_fim = None
        self.finalizado = False          

    def registrar_resposta(self, indice_pergunta, valor):
        pergunta = self.questionario.perguntas[indice_pergunta]
        if pergunta.get_tipo() == "multipla_escolha":
            nova_resposta = RespostaObjetiva(pergunta, valor)
        else:
            nova_resposta = RespostaDiscursiva(pergunta, valor)

        self.respostas.append(nova_resposta)

    def calcular_pontuacao(self):
        total = 0.0
        for resp in self.respostas:
            total += resp.calcular_pontuacao()
        return total

    def finalizar(self):
        self.data_fim = datetime.now() 
        self.finalizado = True
        nota_final = self.calcular_pontuacao()
        
        return (nota_final, "Finalizado")

    def is_finalizado(self):
        return self.finalizado