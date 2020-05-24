lista = []
for x in range(5):
    pessoa = float(input(f'Qual o peso da {x + 1}° pessoa? '))
    lista.append(pessoa)

print(f'O maior peso lido foi de {max(lista):.1f}Kg')
print(f'O menor peso lido foi de {min(lista):.1f}Kg')
