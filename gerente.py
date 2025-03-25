from funcionario import Funcionario

class Gerente(Funcionario):
    def obter_funcao(self):
        return "Gerente"
    
    def calcular_salario(self):
        return 12000

    def esta_disponivel(self):
        return True
