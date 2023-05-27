from time import sleep
def maior(*num):
  print('Analisando os valores passados...')
  sleep(0.5)
  if len(num) == 0:
    print('Foram informados 0 valores ao todo')
    print('O maior valor informado foi 0')
    
  else:
    maior = num[0]
    for i in num:

      if i > maior:
        maior = i

      print(f'{i} ', end = '')

    tam = len(num)
    print(f'Foram informados {tam} valores ao todo')
    print(f'O maior valor foi: {maior}')

  #cálculo do maior valor informado


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
