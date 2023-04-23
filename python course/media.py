nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media >= 7.0:
  print('APROVADO')
elif media < 5.0:
  print('REPROVADO')
else:
  print('RECUPERAÇÃO')
