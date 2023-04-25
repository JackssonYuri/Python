maior = 0
menor = 0
for i in range(1, 6):
  peso = float(input('Peso da {}ª pessoa: '.format(i)))

  if i == 1: #o primeiro é sempre o maior, isso no primeiro laço
    maior = peso
    menor = peso
  else:  #para o segundo laço, analiso se o peso que acabou de ser lido é maior ou menor que o peso que está como maior ou menor já armazenado
    if peso > maior: 
      maior = peso
    if peso < menor:
      menor = peso

print('O maior peso das 5 pessoas é de: {}Kg'.format(maior))
print('O menor peso das 5 pessoas é de: {}Kg'.format(menor))
