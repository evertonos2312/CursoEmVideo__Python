from datetime import date
atual = date.today().year
idade = []
nome = []
for x in range(2):
    n = input(f'Qual o nome da {x + 1}° pessoa? ')
    nas = int(input(f'E em que ano {n} nasceu? '))
    nome.append([n])
#    nome.insert(0, x atual - nas)
print(nome)
print('Resumindo...')
print()
'''
for k in range(len(nome)):
    print(f'{nome[k]} nasceu em {atual - idade[k]} e tem {idade[k]} anos,', end=' ')
    if idade[k] >= 18:
        print(f'então é maior de idade')
    else:
        print(f'então é menor de idade')'''''