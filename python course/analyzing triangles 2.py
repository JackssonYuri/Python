number1 = float(input('Número 1: '))
number2 = float(input('Número 2: '))
number3 = float(input('Número 3: '))

if number1 < number2 + number3 and number2 < number1 + number3 and number3 < number1 + number2:
  print('Forma triângulo')
  if number1 == number2 and number2 == number3:
    print('Equilátero')
  elif number1 != number2 != number3 != number1:
    print('Escaleno')
  else:
    print('Isósceles')
else:
  print('Não forma triângulo')
