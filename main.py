from codigo.bytebank import Funcionario

def teste_idade():
    funcionario = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario.idade()}')

teste_idade()