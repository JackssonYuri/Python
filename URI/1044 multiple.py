A, B = input().split(" ")
A = int(A)
B = int(B)

maior = max(A, B)
menor = min(A, B)

if maior % menor == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
