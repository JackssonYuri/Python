nome = str(input('Nome: ')).strip()

primeiro = nome.split()

ultimo_nome = len(primeiro)
print('Primeiro nome: {}'.format(primeiro[0]))
print('Último nome: {}'.format(primeiro[ultimo_nome-1]))
