nome = str(input('Digite seu nome completo: ')).strip()
print('-=' * 10)
print(f'Muito prazer em te conhecer!')
lista = nome.split()
ultimo = lista[-1]
print(f'Seu primeiro nome é {lista[0]}')
print(f'Seu último nome é {ultimo}')
