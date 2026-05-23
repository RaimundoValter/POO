from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Estagiario aqui.

class Estagiario(Funcionario):
    def _init_(self, nome, matricula, salario_base, curso, carga_horaria):
        super()._init_(nome, matricula, salario_base)
        self.curso = curso
        self.carga_horaria = carga_horaria

    def calcular_bonus(self):
        return self.salario_base * 0.03
    
    def calcular_descontos(self):
        return self.salario_base * 0.02
    
    def calcular_adicionais(self):

        if self.carga_horaria <= 20:
            return self.salario_base + 150.0
        elif self.carga_horaria >20 and self.carga_horaria<=30:
            return self.salario_base + 250.0
        elif self.carga_horaria > 30:
            return self.salario_base + 350.0

    pass
