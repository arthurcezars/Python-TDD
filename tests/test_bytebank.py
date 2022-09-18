from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given-When-Then
        entrada = '13/03/2000' # Given-Contexto
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-Ação

        assert esperado == resultado # Then-Desfecho