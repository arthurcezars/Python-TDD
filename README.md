# TDD com pytest  
  
## Comandos    
* pytest (Executa todos os testes)  
* pytest -v (Executa todos os testes verbosamente)  
* pytest -k parte_do_nome_do_teste (Executa o teste encontrado com base na parte do nome do teste)  
* pytest -m nome_do_mark (Executa todos os testes com o marcador passado)  
* pytest --markers (Listar todos os markers padrões registrados pelo pytest)    
  
Obs.: É possivel usar mais de uma flag.  
  
## Arquivo pytest.ini  
  
O arquivo pytest.ini altera a configuração padrão do pytest, com isso podemos adicionar nossa propria configuração  
como por exemplo os nossos markers pesonalizados. Cuidado para não alterar configurações que possam mudar o  
funcionamento da bliblioteca para um comportamento indesejado.