from bytebank import Funcionario

# lucas = Funcionario("Lucas Carvalho", '13/03/2000', 1000)

# print(lucas.idade())

def teste_idade():
    funcionario = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario.idade()}')

teste_idade()