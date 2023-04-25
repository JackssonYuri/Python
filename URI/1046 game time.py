hora_inicial, hora_final = input('').split()

hora_inicial = int(hora_inicial)
hora_final = int(hora_final)

maior = max(hora_inicial, hora_final)
if hora_inicial == hora_final:
  print('O JOGO DUROU 24 HORA(S)')
elif hora_inicial == maior:
  result = (24 % hora_inicial) + hora_final
  print('O JOGO DUROU {} HORA(S)'.format(result))
elif hora_final == maior:
  result = hora_final - hora_inicial
  print('O JOGO DUROU {} HORA(S)'.format(result))

