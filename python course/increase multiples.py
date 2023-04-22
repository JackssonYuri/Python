salario = float(input('Diga seu salário: '))

if salario > 1250.0:
  novo_salario = salario + (0.1 * salario)
else:
  novo_salario = salario + (0.15 * salario)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, novo_salario))
