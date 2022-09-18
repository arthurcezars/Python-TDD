from codigo.bytebank import Funcionario
import pytest


class TestClass:
    # Passando o nome do metodo para os testes o pytest faz a criação do objeto no momento de execução dos teste
    @pytest.fixture(scope='function')
    def funcionario(self):
        return Funcionario(' Lucas Carvalho ', '13/03/2000', 1111)

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self, funcionario):
        # Given-When-Then
        entrada = '13/03/2000' # Given-Contexto
        esperado = 22

        # funcionario_teste = Funcionario('Teste', entrada, 1111)
        # resultado = funcionario_teste.idade() # When-Ação
        resultado = funcionario.idade() # When-Ação

        assert esperado == resultado # Then-Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self, funcionario):
        # Given-When-Then
        entrada = ' Lucas Carvalho ' # Given-Contexto
        esperado = 'Carvalho'

        # lucas = Funcionario(entrada, '11/11/2000', 1111)
        # resultado = lucas.sobrenome() # When-Ação
        resultado = funcionario.sobrenome() # When-Ação

        assert esperado == resultado # Then-Desfecho