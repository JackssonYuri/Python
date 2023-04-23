from datetime import date

ano_nascimento = int(input('Diga seu ano de nascimento: '))

idade = date.today().year - ano_nascimento

print('Sua idade é: {}'.format(idade))

if idade <= 9:
  print('MIRIM')
elif idade > 9 and idade <= 14: #idade <= 14
  print('INFANTIL')
elif idade > 14 and idade <= 19: #idade <= 19
  print('JUNIOR')
elif idade > 19 and idade <= 25: #idade <= 25
  print('SÊNIOR')
else: 
  print('MASTER')
