from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Estagiario aqui.

class Estagiario(Funcionario):
    def __init__(self, nome, matricula, salario_base, curso, carga_horaria):
        super().__init__(nome, matricula, salario_base)
        if not curso:
            raise ValueError("Curso invalido")
        
        if not carga_horaria:
            raise ValueError("Carga horária inválida")
        
        @property
        def curso(self):
            return self._curso
        
        @curso.setter
        def curso(self, valor):
            self._curso = valor

        @property
        def carga_horaria(self):
            return self._carga_horaria    

        @carga_horaria.setter
        def carga_horaria(self, valor):
            if valor <= 0:
                raise ValueError("Quantidade de horas da carga horaria invalida")
            self._carga_horaria = valor 


    def calcular_bonus(self):
        return self.salario_base * 0.03

    def calcular_descontos(self):
        return self.salario_base * 0.02

    def calcular_adicionais(self):
        if self.carga_horaria <= 20:
            return 150
        elif self.carga_horaria <= 30:
            return 250
        return 350
    