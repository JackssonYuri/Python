import random 
print('-'*20)
print('------JOKENPÔ-------')
print('-'*20)

lista = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(lista)

#print(computador)

usuario = int(input('Escolha uma opção\n1 - Pedra\n2 - Papel\n3 - Tesoura\nDigite a opção: '))

if usuario == 1 and computador == 'Tesoura':
  print('Você ganhou, o computador escolheu: {}'.format(computador))
elif usuario == 1 and computador == 'Papel':
  print('Você perdeu, o computador escolheu: {}'.format(computador))
elif usuario == 1 and computador == 'Pedra':
  print('Empate, o computador escolheu: {}'.format(computador))
elif usuario == 2 and computador == 'Tesoura':
  print('Você perdeu, o computador escolheu: {}'.format(computador))
elif usuario == 2 and computador == 'Papel':
  print('Empate, o computador escolheu: {}'.format(computador))
elif usuario == 2 and computador == 'Pedra':
  print('Você ganhou, o computador escolheu: {}'.format(computador))
elif usuario == 3 and computador == 'Tesoura':
  print('Empate, o computador escolheu: {}'.format(computador))
elif usuario == 3 and computador == 'Pedra':
  print('Você perdeu, o computador escolheu: {}'.format(computador))
elif usuario == 3 and computador == 'Papel':
  print('Você ganhou, o computador escolheu: {}'.format(computador))
