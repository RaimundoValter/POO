from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Gerente aqui.

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, setor, qtd_equipe):
        super().__init__(nome, matricula, salario_base)
        
        # Verificação do setor
        if not setor:
            raise ValueError("Setor Invalido")
        
        # Verificação da quantidade da equipe
        if not qtd_equipe:
            raise ValueError("Quantidade de membros da equipe inválida")
        
        @property
        def setor(self):
            return self._setor
        
        @setor.setter
        def setor(self, valor):
            self._setor = valor

        @property
        def qtd_equipe(self):
            return self._qtd_equipe

        @qtd_equipe.setter
        def qtd_equipe(self, valor):
            if valor <= 0:
                raise ValueError("Quantidade invalida de membros da equipe")
            self._qtd_equipe = valor    
        
    def calcular_bonus(self):
        if self.qtd_equipe <= 5:
            return self.salario_base * 0.10
        
        elif self.qtd_equipe <= 10:
            return self.salario_base * 0.15
        
        else:
            return self.salario_base * 0.20
        
    def calcular_descontos(self):
        return self._salario_base * 0.12
    
    def calcular_adicionais(self):
        if self.qtd_equipe > 10:
            return 2000
        elif self.qtd_equipe > 5:
            return 1000
        else:
            return 500

    
    