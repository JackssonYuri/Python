a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

maior = a
if b > a and b > c:
  maior = b
if c > b and c > a:
  maior = c

menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c

meio = a 
if b != maior and b != menor:
  meio = b
if c != maior and c != menor: 
  meio = c
print('{}'.format(menor))
print('{}'.format(meio))
print('{}\n'.format(maior))

print('{}'.format(a))
print('{}'.format(b))
print('{}'.format(c))
