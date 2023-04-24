s = 0
for i in range(0, 6):
  number = int(input('Digite um valor: '))
  if number % 2 == 0:
    s += number
print('A soma dos números pares é de: {}'.format(s))
