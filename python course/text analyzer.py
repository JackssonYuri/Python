nome = str(input('Digite seu nome completo: ')).strip()

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_tamanho = len(nome)
dividido = nome.split()

cont = nome.count(' ')

print('Nome maiúsculo: {}'.format(nome_maiusculo))
print('Nome minúsculo: {}'.format(nome_minusculo))
print('Tamanho do nome: {}'.format(nome_tamanho-cont))
print('Tamanho do primeiro nome: {}'.format(len(dividido[0])))
#print('Tamanho do primeiro nome: {}'.format(nome.find(' ')))
