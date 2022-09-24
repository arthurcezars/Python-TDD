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

        # Sem fixture
        # funcionario_teste = Funcionario('Teste', entrada, 1111)
        # resultado = funcionario_teste.idade() # When-Ação

        # Com fixture
        resultado = funcionario.idade() # When-Ação

        assert esperado == resultado # Then-Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self, funcionario):
        # Given-When-Then
        entrada = ' Lucas Carvalho ' # Given-Contexto
        esperado = 'Carvalho'

        # Sem fixture
        # lucas = Funcionario(entrada, '11/11/2000', 1111)
        # resultado = lucas.sobrenome() # When-Ação

        # Com fixture
        resultado = funcionario.sobrenome() # When-Ação

        assert esperado == resultado # Then-Desfecho

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self, funcionario):
        # Given-When-Then
        entrada_salario = 100000 # Given-Contexto
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        # Sem fixture
        funcionario_teste = Funcionario(entrada_nome, '13/03/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # When-Ação
        resultado = funcionario_teste.salario

        # Com fixture
        # funcionario.decrescimo_salario() # When-Ação
        # resultado = funcionario.salario

        assert esperado == resultado # Then-Desfecho

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self, funcionario):
        # Given-When-Then
        entrada = 1000 # Given-Contexto
        esperado = 100

        # Sem fixture
        funcionario_teste = Funcionario('Ana', '13/03/1997', entrada)
        resultado = funcionario_teste.calcular_bonus() # When-Ação

        # Com fixture
        # resultado = funcionario.calcular_bonus() # When-Ação

        assert esperado == resultado # Then-Desfecho

    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self, funcionario):
        # O pytest considera implicitamente o erro como o esperado
        with pytest.raises(Exception):
            # Given-When-Then
            entrada = 100000000 # Given-Contexto

            # Sem fixture
            funcionario_teste = Funcionario('Ana', '13/03/1997', entrada)
            resultado = funcionario_teste.calcular_bonus() # When-Ação

            # Com fixture
            # resultado = funcionario.calcular_bonus() # When-Ação

            assert resultado # Then-Desfecho