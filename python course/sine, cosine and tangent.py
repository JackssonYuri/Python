import math as ma 

valor = float(input())

seno = ma.sin(valor)
coseno = ma.cos(valor)
tangente = ma.tan(valor)

print('Para o ângulo {}\nO seno é: {:.3f}\nO coseno é: {:.3f}\nA tangente é: {:.3f}'.format(valor, seno, coseno, tangente))
