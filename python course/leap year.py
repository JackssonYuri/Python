from datetime import date #Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto, exceto anos múltiplos de 100 que não são múltiplos de 400
ano = int(input('Que ano quer analisar? Digite 0 para anlisar o ano atual: '))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('O ano de {} é um ano BISSEXTO'.format(ano))
else:
  print('O ano de {} não é um ano BISSEXTO'.format(ano))
