musculatura = str(input(""))
tipo = str(input(""))
alimentacao = str(input(""))

if musculatura == 'vertebrado': 
  if tipo == 'ave':
    if alimentacao == 'carnivoro':
      print('aguia')
    elif alimentacao == 'onivoro':
      print('pomba')
  elif tipo == 'mamifero':
    if alimentacao == 'onivoro':
      print('homem')
    elif alimentacao == 'herbivoro':
      print('vaca')

elif musculatura == 'invertebrado':
  if tipo == 'inseto':
    if alimentacao == 'hematofago':
      print('pulga')
    elif alimentacao == 'herbivoro':
      print('lagarta')
  elif tipo == 'anelideo':
    if alimentacao == 'hematofago':
      print('sanguessuga')
    elif alimentacao == 'onivoro':
      print('minhoca')


