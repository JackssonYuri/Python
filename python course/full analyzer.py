soma_idade = 0
cont = 0
maior_idade = 0
nomevelho = ''
for i in range(1,5):
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo: ')).strip()
  soma_idade += idade

  if i == 1 and sexo in 'Mm':
    maior_idade = idade
    nomevelho = nome
  if sexo in 'Mm' and idade > maior_idade:
    maior_idade = idade
    nomevelho = nome
  if sexo in'Ff'and idade < 20:
    cont += 1


print('A média das idades é {}'.format(soma_idade/4))
print('O homem mais velho tem {} anos e o nome dele é {}'.format(maior_idade, nomevelho))
print('O total de mulher com menos de 20 anos é: {}'.format(cont))



