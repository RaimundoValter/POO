from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Gerente aqui.

class Gerente(Funcionario):
    def _init_(self, nome, matricula, salario_base, setor, qtd_equipe):
        super()._init_(nome, matricula, salario_base)
        self.setor = setor
        self.qtd_equipe = qtd_equipe

    def calcular_bonus(self):

        if self.setor <= 5:
            return self.salario_base * 0.10
        elif self.setor > 5 and self.qtd_equipe <=10:
            return self.salario_base * 0.15
        elif self.setor > 10:
            return self.salario_base * 0.15

        return 0.0

    def calcular_descontos(self):
        return self.salario_base * 0.12

    def calcular_adicionais(self):
       
        if self.qtd_equipe > 10:
            return self.salario_base + 2000.0
        elif self.qtd_equipe > 5:
            return self.salario_base + 1000.0

        return self.salario_base + 500.0
    
    pass
