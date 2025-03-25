from funcionario import Funcionario

class FuncionarioNulo(Funcionario):
    def obter_funcao(self):
        return "Nenhum funcionário disponível"
    
    def calcular_salario(self):
        return 0

    def esta_disponivel(self):
        return False
