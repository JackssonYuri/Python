idade = int(input())

ano = idade // 365

idade %= 365

mes = idade // 30


idade %= 30

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{idade} dia(s)')
