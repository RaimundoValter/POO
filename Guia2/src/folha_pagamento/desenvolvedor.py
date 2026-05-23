from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Desenvolvedor aqui.

class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, linguagem, senioridade):
        super().__init__(nome, matricula, salario_base)
        self.linguagem = linguagem
        self.senioridade = senioridade
    
    def calcular_bonus(self):
        if self.senioridade == "junior":
            return self.salario_base * 0.05
        if self.senioridade == "pleno":
            return self.salario_base * 0.10
        if self.senioridade == "senior":
            return self.salario_base * 0.15
    
    def calcular_descontos(self):
        return 0.08 * self.salario_base
    
    def calcular_adicionais(self):
        if self.linguagem == "Python":
            return 500
        if self.linguagem == "Java":
            return 400
        if self.linguagem == "JavaScript":
            return 350
        else:
            return 200