nome = input('Qual é seu nome?')
print('Prazer em te conhecer {:^20}!'.format(nome)) #centralizado em 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome)) #alinhado a direita em 20 espaços
print('Prazer em te conhecer {:<20}!'.format(nome)) #alinhado a esquerda em 20 espaços
print('Prazer em te conhecer {:=^20}!'.format(nome)) #centralizado colocando =
