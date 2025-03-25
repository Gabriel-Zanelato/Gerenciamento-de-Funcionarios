from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def obter_funcao(self):
        pass
    
    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def esta_disponivel(self):
        pass

