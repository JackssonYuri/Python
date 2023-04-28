sexo = ' '
sexo = str(input('Diga seu sexo: [M/F] ')).strip().upper()[0] #pego só a primeira letra
while sexo not in 'MmFf':
  sexo = str(input('Digite novamente: [M/F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

# sexo_masculino = 'M'
# sexo_feminino = 'F'
# while sexo_masculino == 'M' and sexo_feminino == 'F':
#   sexo_masculino = str(input('Sexo: '))
#   while sexo_masculino != 'M' or sexo_feminino != 'F':
#     sexo_masculino = str(input('Digite novamente: '))
