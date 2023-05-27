preco = float(input('Preço do produto: '))
forma_pagamento = int(input('Forma de pagamento:\n1 - Dinheiro\n2 - Cheque\n3 - Cartão\nDigite uma opção: '))


if forma_pagamento == 1 or forma_pagamento == 2:
  preco_total = preco - (0.1 * preco)
  print('O valor do produto será de: {:.2f}'.format(preco_total))
elif forma_pagamento == 3:
  parcelas = int(input('Em quantas vezes?\n1 - À vista\n2 - Em até 2x\n3 - Em 3x ou mais\nDigite uma opção: '))
  if parcelas == 1:
    preco_total = preco - (0.05 * preco)
    print('O valor do produto será de: {:.2f}'.format(preco_total))
  elif parcelas == 2:
    print('O valor do produto será de: {:.2f}'.format(preco))
  elif parcelas == 3:
    preco_total = preco + (0.2 * preco)
    print('O valor do produto será de: {:.2f}'.format(preco_total))
else:
  print('Digite novamente!')

