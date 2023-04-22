import random

number =  random.randint(0,5) #Faz o computador "PENSAR"

print('!-' * 11)
print('Tente acertar o número')
print('!-' * 11)

escolha = int(input('Digite o número:'))

# if escolha == number: 
#   print('Você acertou!')
# else:
#   print('Errou!')

print('Acertou' if escolha == number else 'Errou')
