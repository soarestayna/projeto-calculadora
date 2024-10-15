# Projeto Calculadora EBAC

 ## Calculadora criada em linguagem Python executável no ambiente Shell Script.
 * Para executar será necessário:
   
	 1. Acesso ao Linux ou sistemas que rodem uma distribuição Linux;
	 2. Que o ambiente tenha Python instalado;
	 3. Caso não tenha o Python instalado, siga os comandos abaixo:


	   sudo apt update
	   sudo apt install python3

Após entrar no seu ambiente escolhido abra o diretorio que você salvou o script da calculadora.
    Execute a calculadora com o comando:
    
    ./calculadora.sh


## Sobre o código.
O código foi criado para ser semelhante a uma calculadora de desktop com os operadores aritméticos simples, especiais e também acrescentei um operador para conversão de unidades, a sua estrutura foi criada para interagir com o usuário e é composta por um loop, criado com while True, onde só será encerrado por opção do usuário.

* Foi definido um menu onde o usuário poderá escolher a operação que deseja:

      1. Adição
      2. Subtração
      3. Multiplicação
      4. Divisão
      5. Potenciação
      6. Raiz Quadrada
      7. Fatorial
      8. Seno
      9. Cosseno
      10. Tangente
      11. Logaritmo
      12. Conversor de unidades
      0. Sair

Após escolher sua opção, o código mostrará o resultado e continuará sendo executado:

     Calcular novamente? (S/N)

A Opção sendo "S" o loop retornará ao menu, caso seja "N", aparecerá a mensagem de despedida:

    Obrigada por usar a calculadora!
