distancia_viagem = float(input('Digite a distância da viagem: '))

if distancia_viagem <= 200:
  preco_passagem = distancia_viagem * 0.5
  print('O preço da viagem é: R${:.2f}'.format(preco_passagem))
else:
  preco_passagem = distancia_viagem * 0.45
  print('O preço da viagem é: R${:.2f}'.format(preco_passagem))
