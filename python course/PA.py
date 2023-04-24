primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo = primeiro_termo + (10-1) * razao
for i in range(primeiro_termo,decimo_termo, razao):
  if i == primeiro_termo:
    print('{}'.format(primeiro_termo))
  elif i != primeiro_termo:
    print('{} + {} = {}'.format(i-razao, razao, i))
