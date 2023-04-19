import random

Aluno1 = str(input("Aluno 1: "))
Aluno2 = str(input("Aluno 2: "))
Aluno3 = str(input("Aluno 3: "))
Aluno4 = str(input("Aluno 4: "))
lista = [Aluno1, Aluno2, Aluno3, Aluno4]

escolhido = random.choice(lista)

print('O aluno escolhido foi: {}'.format(escolhido))
