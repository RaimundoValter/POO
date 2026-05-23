from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Desenvolvedor aqui.

class Desenvolvedor(Funcionario):
    def _init_(self, nome, matricula, salario_base, linguagem, senioridade):
        super()._init_(nome, matricula, salario_base)
        self.linguagem = linguagem
        self.senioridade = senioridade

    def calcular_bonus(self):
        nivel = self.senioridade.lower()

        if nivel == "junior":
            return self.salario_base * 0.05
        elif nivel == "pleno":
            return self.salario_base * 0.10
        elif nivel == "senior":
            return self.salario_base * 0.15

        return 0.0

    def calcular_descontos(self):
        return self.salario_base * 0.08

    def calcular_adicionais(self):
        ling = self.linguagem.lower()

        if ling == "python":
            return self.salario_base + 500.0
        elif ling == "java":
            return self.salario_base + 400.0
        elif ling == "javascript":
            return self.salario_base + 350.0
    
    pass