velocidade_carro = float(input('Velocidade do carro: '))

if velocidade_carro > 80:
  multa = (velocidade_carro % 80) * 7
  print('Você foi multado!\nSua multa é de R${:.2f}'.format(multa))

print('---FIM---')
