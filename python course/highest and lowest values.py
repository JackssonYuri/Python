a = int(input('Número 1: '))
b = int(input('Número 2: '))
c = int(input('Número 3: '))

menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c
maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c
print('Menor valor é: {}'.format(menor))
print('Maior valor é: {}'.format(maior))
