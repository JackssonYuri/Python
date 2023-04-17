A, B, C, D = input("").split(" ")
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if ( B > C ) & (D > A ) & ((C + D) > ( A+B)) & (C > 0) & (D > 0) & (A % 2 == 0):
  print("Valores aceitos")
else:
  print("Valores nao aceitos")
