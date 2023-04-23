number = int(input('Digite o número inteiro: '))
opcao = int(input('Para qual base de conversão deseja converter o número?\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n\nDigite a opção: '))

if opcao == 1: 
  binary = bin(number)
  print('O número {} em binário fica: {}'.format(number, binary))

elif opcao == 2:
  octal = oct(number)
  print('O número {} em octal fica: {}'.format(number, octal))
elif 3:
  hexadecimal = hex(number)
  print('O número {} em hexadecimal fica: {}'.format(number, hexadecimal))
