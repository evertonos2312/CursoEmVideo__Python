sidade = 0
media = 0
nomev = ''
maioridadeh = 0
ran = 5
totmulher = 0
for p in range(1, ran):
    print(f'----- {p}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    sidade += idade
    if p == 1 and sexo == 'M':
        maioridadeh = idade
        nomev = nome
    if sexo == 'M' and idade > maioridadeh:
        maioridadeh = idade
        nomev = nome
    if sexo == 'F' and idade < 20:
        totmulher += 1
media = sidade / (ran - 1)
print(f'A média de idade do grupo é de {int(media)} anos.')
print(f'O homem mais velho tem {maioridadeh} anos e se chama {nomev}. ')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos.')
