A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

PI = 3.14159

TRIANGULO = (A * C)/2
CIRCULO = PI * (C * C)
TRAPEZIO = (A+B)/2 * C
QUADRADO = B * B
RETANGULO = A * B 


print("TRIANGULO: %0.3f" %TRIANGULO)
print("CIRCULO: %0.3f" %CIRCULO)
print("TRAPEZIO: %0.3f" %TRAPEZIO)
print("QUADRADO: %0.3f" %QUADRADO)
print("RETANGULO: %0.3f" %RETANGULO)
