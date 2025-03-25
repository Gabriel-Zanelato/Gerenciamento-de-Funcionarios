from funcionario_nulo import FuncionarioNulo
from gerente import Gerente
from desenvolvedor import Desenvolvedor
from analista import Analista


class RepositorioFuncionarios:
    def __init__(self):
        self.funcionarios = {
            1: Gerente(),
            2: Desenvolvedor(),
            3: Analista()
        }
    
    def buscar_funcionario(self, id_funcionario):
        return self.funcionarios.get(id_funcionario, FuncionarioNulo())
