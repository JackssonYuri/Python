print('-'*19)
print('EMPRÉSTIMO BANCÁRIO')
print('-'*19)

valor_casa = float(input('Valor da casa: '))
salario = float(input('Seu salário: '))
anos = int(input('Em quantos anos pretende pagar? '))

prestacao = valor_casa / (anos * 12)
# prestacao_anual = valor_casa / anos 
# prestacao_mensal = prestacao_anual / 12

# minimo = salario * 30 / 100(30%)
if prestacao > 0.3 * salario:
  print('Empréstimo negado!')
else: 
  print('Seu empréstimo foi aprovado!\nPrestação total é de: R${:.2f}'.format(prestacao))
