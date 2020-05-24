soma = 0
cont = 0
x = int(input())
y = int(input())
for c in range(x, y + 1, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')
