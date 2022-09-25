# TDD com pytest  
  
## Comandos pytest    
* pytest (Executa todos os testes)  
* pytest -v (Executa todos os testes verbosamente)  
* pytest -k parte_do_nome_do_teste (Executa o teste encontrado com base na parte do nome do teste)  
* pytest -m nome_do_mark (Executa todos os testes com o marcador passado)  
* pytest --markers (Listar todos os markers padrões registrados pelo pytest)    
* pytest --cov (Executa todos os testes e retorna um relatorio da cobertura do codigo)   
* pytest --cov=diretorio_ou_arquivo tests/ (Passa o diretorio ou arquivo com o codigo para verificar)  
* pytest --cov=diretorio_ou_arquivo tests/ --cov-report term-missing (Indica os termos faltantes para atingir 100% de cobertura) 
* pytest --cov=diretorio_ou_arquivo tests/ --cov-report html (Gera o relatorio da cobertura de testes em html)   
* pytest --junitxml report.xml (Gera o relatorio da cobertura de testes em xml)   
* pytest --cov-report xml (Gera o relatorio da cobertura de testes em xml)   
  
Obs.: É possivel usar mais de uma flag.  
  
## Arquivo pytest.ini  
  
O arquivo pytest.ini altera a configuração padrão do pytest, com isso podemos adicionar nossa propria configuração  
como por exemplo os nossos markers pesonalizados. Cuidado para não alterar configurações que possam mudar o  
funcionamento do framework para um comportamento indesejado.   
   
## Arquivo .coveragerc   
   
O arquivo .coveragerc altera a configuração do pytest-cov, nele nós podemos por exemplo indicar quais metódos não 
precisamos cobrir nos nossos testes e assim quando gerar o relatorio ele não vai indicar o método como não coberto.  
Outro exemplo é inserir a configuração source = ./codigo que faz com que ao executar o comando pytest --cov ele passe 
a executar o teste de cobertura somente no diretorio codigo e não mais em todos os arquivos.      