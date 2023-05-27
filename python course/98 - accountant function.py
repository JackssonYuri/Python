from time import sleep

def contador(i, f, p):
  if p < 0:
    p *= -1
  if p == 0:
    p = 1
  print(f'Contagem de {i} até {f} de {p} em {p}')
  if i < f:
    cont = i #inicio
    while cont <= f:
      print(f'{cont} ', end = '', flush=True) #flush n ligar o buffer
      sleep(0.5)
      cont +=p
    print('FIM!')
  else:
    cont = i
    while cont >= f:
      print(f'{cont} ', end = '',flush=True)
      sleep(0.5)
      cont -=p
    print('FIM!')


# Programa principal
contador(1,10,1)
contador(10,0,2)
print(f'Agora é sua vez de personalizar!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
  
    
