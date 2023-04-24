number = int(input('Digite um número inteiro: '))
tot = 0
for i in range (1,number+1):
  if number % i == 0 :
    tot += 1
print('O número {} foi dividido {} vezes'.format(number, tot))

if tot == 2:
  print('E por isso ele é primo')
else: 
  print('Não é primo')
