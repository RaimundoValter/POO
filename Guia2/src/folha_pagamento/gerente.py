from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Gerente aqui.

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, setor, qtd_equipe):
        super().__init__(nome, matricula, salario_base)
        if not setor:
            raise ValueError("Sem valor")
        if not qtd_equipe or qtd_equipe <= 0:
            raise ValueError("Sem valor ou valor incorreto")
        self.setor = setor
        self.qtd_equipe = qtd_equipe

    def calcular_bonus(self):
        if self.qtd_equipe <= 5:
            return self.salario_base * 0.1
        elif self.qtd_equipe > 5 and self.qtd_equipe <= 10:
            return self.salario_base * 0.15
        elif self.qtd_equipe > 10:
            return self.salario_base * 0.2 
        
    def calcular_descontos(self):
        return self.salario_base * 0.12
        
    def calcular_adicionais(self):
        
        if self.qtd_equipe > 10:
            return 2000
        elif self.qtd_equipe > 5:
            return 1000
        else:
            return 500
