from funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def obter_funcao(self):
        return "Desenvolvedor"
    
    def calcular_salario(self):
        return 9000

    def esta_disponivel(self):
        return True
