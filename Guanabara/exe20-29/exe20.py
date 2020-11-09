from random import shuffle
nome = []

while len(nome) < 4:
    name = input('Digite o nome do aluno: ')
    nome.append(name)
shuffle(nome)
print('A ordem de apresentação será: ')
print(nome)
