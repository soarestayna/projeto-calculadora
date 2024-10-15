import math

nome = input('Digite seu nome: ')
print('Seja bem-vindo(a),',nome, '!')

def menu():
 print('O que vamos calcular hoje?')
 print('1. Adição')
 print('2. Subtração')
 print('3. Multiplicação')
 print('4. Divisão')
 print('5. Potenciação')
 print('6. Raiz Quadrada')
 print('7. Fatorial')
 print('8. Seno')
 print('9. Cosseno')
 print('10. Tangente')
 print('11. Logaritmo')
 print('12. Conversor de Unidades')
 print('0. Sair')

def metro_para_quilometros(metro):
 return metro / 1000

def celsius_para_fahrenheit(celsius):
 return (celsius * 9/5) + 32

def quilogramas_para_gramas(quilogramas):
 return quilogramas * 1000

def menu_conversao():
 print('Escolha a opção de conversão: ')
 print('1. Metro para Quilômetro')
 print('2. Celsius para Fahrenheit')
 print('3. Quilogramas para Gramas')

r = 'S'
while r.upper() == 'S':
 menu()
 opcao = int(input('Digite sua opção: '))

 if opcao == 0:
  print('Saindo da calculadora, até a próxima!')
  break

 if opcao < 1 or opcao > 12:
  print('Opção inválida! Escolha um número da lista.')
  continue
 
 if opcao != 12:
  num1 = float(input('Digite um número: '))

 if opcao != 6 and opcao != 7 and opcao != 8 and opcao != 9 and opcao != 10 and opcao != 11 and opcao != 12:
  num2 = float(input('Digite outro número: '))
 
 if opcao == 1:
  resultado = num1 + num2
 elif opcao == 2:
  resultado = num1 - num2
 elif opcao == 3:
  resultado = num1 * num2
 elif opcao == 4:
  if num2 == 0:
   print('Erro: divisão por zero')
   continue
   resultado = num1 / num2
 elif opcao == 5:
  resultado =  num1 ** num2
 elif opcao == 6:
  resultado = math.sqrt(num1)
 elif opcao == 7:
  resultado = math.factorial(int(num1))
 elif opcao == 8:
  resultado = math.sin(math.radians(num1))
 elif opcao == 9:
  resultado = math.cos(math.radians(num1))
 elif opcao == 10:
  resultado = math.tan(math.radians(num1))
 elif opcao == 11:
  if num1 <= 0:
   print('Erro: logaritmo de número negativo ou zero.')
   continue
   resultado = math.log(num1)
 elif opcao == 12:
  menu_conversao()
  opcao_conversao = input('Digite sua opção de conversão: ')
  valor = float(input('Digite o valor a ser convertido: '))
  if opcao_conversao == '1':
   resultado = metros_para_quilometros(valor)
  elif opcao_conversao == '2':
   resultado = celsius_para_fahrenheit(valor)
  elif opcao_conversao == '3':
   resultado = quilogramas_para_gramas(valor)
  else:
   print('Opção de conversão inválida.')
   continue
  
 if opcao != 12:
  print('O resultado da operação é: ', resultado)
 else:
  print('O resultado da conversão é: ', resultado)

 r = input('Calcular novamente? (S/N): ').upper()

print('Obrigada por usar a calculadora!')
