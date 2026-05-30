from folha_pagamento.funcionario import Funcionario

class Desenvolvedor(Funcionario):

    def __init__(self, nome, matricula, salario_base, linguagem, senioridade):
        super().__init__(nome, matricula, salario_base)
        self._linguagem = linguagem
        self._senioridade = senioridade

    @property
    def linguagem(self):
        return self._linguagem

    @linguagem.setter
    def linguagem(self, valor):
        self._linguagem = valor

    @property
    def senioridade(self):
        return self._senioridade

    @senioridade.setter
    def senioridade(self, valor):
        self._senioridade = valor

    def calcular_bonus(self):

        if self.senioridade == 'junior':
            return self.salario_base * 0.05

        elif self.senioridade == 'pleno':
            return self.salario_base * 0.10

        elif self.senioridade == 'senior':
            return self.salario_base * 0.15

        return 0

    def calcular_descontos(self):
        return self.salario_base * 0.08

    def calcular_adicionais(self):

        if self.linguagem == 'Python':
            return 500

        elif self.linguagem == 'Java':
            return 400

        elif self.linguagem == 'JavaScript':
            return 350

        else:
            return 200
        