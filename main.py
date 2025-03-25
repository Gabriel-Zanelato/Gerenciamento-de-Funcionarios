from repositorio_funcionarios import RepositorioFuncionarios

repositorio = RepositorioFuncionarios()

funcionario1 = repositorio.buscar_funcionario(1)
print(f"Função: {funcionario1.obter_funcao()}, Salário: {funcionario1.calcular_salario()}, Disponível: {funcionario1.esta_disponivel()}")

funcionario_nulo = repositorio.buscar_funcionario(99)
print(f"Função: {funcionario_nulo.obter_funcao()}, Salário: {funcionario_nulo.calcular_salario()}, Disponível: {funcionario_nulo.esta_disponivel()}")

