valor = int(input('Digite um valor: '))
print("-" * 13)
for i in range (1,11):
  tabuada = valor * i
  print('{} * {:2} = {}'.format(valor, i, tabuada))
print("-" * 13)
