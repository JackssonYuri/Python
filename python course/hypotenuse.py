import math

cateto_oposto = float(input())
cateto_adjacente = float(input())

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
#hipoenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 1/2

print('Hipotenusa é: {:.2f}'.format(hipotenusa))
