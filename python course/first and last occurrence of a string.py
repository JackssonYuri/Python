frase = str(input('Frase: ')).upper().strip()

print('A aparece: {}'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #começa procurando pela direita

