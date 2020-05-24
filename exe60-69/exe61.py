print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
ultimo = int(input('Último elemento da PA: '))
termo = primeiro
cont = 1
while cont <= ultimo:
    print(f'{termo} --> ', end='')
    termo += razao
    cont += primeiro
print('FIM')
