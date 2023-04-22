A, B, C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)

if A < B + C and B < A + C and C < A + B:
  print('Perimetro = {:.1f}'.format(A + B + C))
else:
  print('Area = {}'.format(((A + B) * C )/2))
