from datetime import date

ano_nascimento = int(input('Diga seu ano de nascimento: '))

idade = date.today().year - ano_nascimento

print('Sua idade é: {}'.format(idade))

if idade > 18:
  tempo = idade - 18 #idade % 18
  print('Já passou do tempo de alistamento em {} ano(s)'.format(tempo))
elif idade == 18:
  print('Está na hora de se alistar!')
else: 
  tempo = 18 - idade
  print('Você ainda vai se alistar daqui {} ano(s)'.format(tempo))
