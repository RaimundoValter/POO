from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Desenvolvedor aqui.

class Desenvolvedor(Funcionario):
    def __init__(self, nome: str, matricula: str, salario_base: float, linguagem, senioridade):
        super().__init__(nome,matricula,salario_base)
        self.linguagem = linguagem
        self.senioridade = senioridade
    
    def calcular_bonus(self):
        if self.senioridade.lower() == "junior":
            return self.salario_base *0.05
        
        if self.senioridade.lower() == "pleno":
            return self.salario_base *0.10
        
        if self.senioridade.lower() == "senior":
            return self.salario_base *0.15
    
    def calcular_descontos(self):
        return self.salario_base *0.08
    
    def calcular_adicionais(self):
        if self.linguagem.lower() == "python":
            return 500 
        elif self.linguagem.lower() == "java":
            return 400
        elif self.linguagem.lower() == "javascript":
            return 350 
        else:
            return 200 