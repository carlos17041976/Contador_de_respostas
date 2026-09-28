<h1 align="center"> CONTADOR DE RESPOSTAS  </h1> 

<div align="center">
  <img src="logo.png" alt="Texto alternativo" width="400">
</div>

## Índice
* [Nome e objetivo do sistema](#nome-e-objetivo-do-sistema)
* [Linguagem usada (Python)](#linguagem-usada)
* [Instruções para executar o programa](#instruções-para-executar-o-programa)

## Nome e objetivo do sistema
### Nome do sistema é Contador de Respostas. O programa deve solicitar a digitação do nome, idade e opinião do entrevistado(a) sobre o atendimento prestado, sendo:
1. EXCELENTE
2. BOM
3. RUIM
### A pesquisa deve ser feita com 50 entrevistados. Ao final, o programa deverá exibir na tela:
a) Quantidade de respostas "EXCELENTE"<br>
b) Quantidade de respostas "BOM"<br>
c) Quantidade de respostas "RUIM"<br>
       
## Linguagem usada
### A linguagem utilizada é o Python. 

## Instruções para executar o programa
### O(A) operador(a) do sistema deve lançar os dados por ordem conforme orientação do próprio sistema, ou seja, nome, em seguida a idade e por fim, a avalição referente o atendimento.
### O sistema é auto intuitivo. Ele mesmo diz o que o(a) operador(a) deve fazer.
### Apesar do sistema comportar até 50 entrevistados, a fim de expedir relatório ao número de 10, então foi necessário antes alterar o seguinte campo para "10"
for i in range(1, 51):

    print(f"\n--- Entrevistado {i} de 50 ---")
### Automaticamente quando o sistema atinge o valor de 10 entrevistados, emite o relatório solicitado como mostra a seguir:
========== RESULTADO DA PESQUISA ==========<br>
EXCELENTE: 4<br>
BOM:       3<br>
RUIM:      2<br>

<h1>
<br>
<br>
<h1>

<div align="center">
  <img src="logo2.png" alt="Texto alternativo" width="400">
</div>