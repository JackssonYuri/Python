peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))

imc = peso / (altura * altura) #altura ** 2

print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
  print('Abaixo do peso')
elif imc >= 18.5 and imc < 25: # 18.5 <= imc < 25
  print('Peso ideal')
elif imc >= 25.0 and imc < 30:
  print('Sobrepeso')
elif imc >= 30.0 and imc < 40:
  print('Obesidade')
else: 
  print('Obesidade mórbida')
