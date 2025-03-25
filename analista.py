from funcionario import Funcionario

class Analista(Funcionario):
    def obter_funcao(self):
        return "Analista"
    
    def calcular_salario(self):
        return 7000

    def esta_disponivel(self):
        return True
