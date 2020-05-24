from random import choice

lista = []

while len(lista) < 4:
    nome = input('Digite o nome do aluno: ')
    lista.append(nome)

escolha = choice(lista)
print(f'O aluno escolhido foi o {escolha}')
