from datetime import date

atual = date.today().year

maior = 0
menor = 0
for i in range(0,7):
  nasc = int(input('Ano de nascimento: '))
  idade = atual - nasc
  if idade >= 18:
    maior += 1
  else: 
    menor +=1
print('A quantidade de pessoas maior de idade é de: {}'.format(maior))
print('A quantidade de pessoas menor de idade é de: {}'.format(menor))
