from random import randint

number =  random.randint(0,10) #Faz o computador "PENSAR"

print('!-' * 11)
print('Tente acertar o número')
print('!-' * 11)

digitado = 0
cont = 1

#print(number) #número que o computador pensou
digitado = int(input('Digite o número: '))
if digitado == number:
  print('Você acertou!Seu número de tentativas foi de: {}'.format(cont))
while digitado != number:
  if digitado > number:
    print('Menos...Você errou, digite novamente!')
  else:
    print('Mais...Você errou, digite novamente!')

  digitado = int(input('Digite o número: '))
  cont+=1
  if digitado == number:
    print('Você acertou!\nSeu número de tentativas foi de: {}'.format(cont))
