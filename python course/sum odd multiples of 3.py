s = 0
for i in range(1, 500+1):
  if i % 1 == 0 and i % 3 == 0:
    s += i
print('A soma é de: {}'.format(s))
print('FIM')
