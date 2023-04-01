class Triangulo: 
  def __init__(self, lado1, lado2, lado3,base, altura):
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3 
    self.base = base
    self.altura = altura

  def area(self): #o self aqui é padrão
    return (self.base * self.altura) / 2 #preciso do self para acessar atributos lá de cima

  def tipo(self):
    if self.lado1 < self.lado2 + self.lado3:
      return 'não e um triângulo'
    elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado1 == self.lado2:
      return 'triângulo isósceles'
    else: 
      return 'outro tipo de triângulo'

t1 = Triangulo(2,1,3,4,3)

t1.tipo()
t1.area()
print(t1.lado1, t1.lado2, t1.lado3, t1.base, t1.altura)

t2 = Triangulo(8,8,8, 16,9)

t2.tipo()
t2.area()
print(t2.lado1, t2.lado2, t2.lado3, t2.base, t2.altura)
