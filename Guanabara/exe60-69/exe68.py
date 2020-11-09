from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    cpu = randint(0, 11)
    total = jogador + cpu
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou \033[34m{jogador}\033[m e o computador \033[34m{cpu}\033[m. '
          f'Total de \033[34m{total}\033[m → ', end='')
    print('DEU \033[34mPAR\033[m' if total % 2 == 0 else 'DEU \033[34mÍMPAR\033[m')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você \033[34mVENCEU!\033[m')
            v += 1
        else:
            print('Você \033[31mPERDEU!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você \033[34mVENCEU!\033[m')
            v += 1
        else:
            print('Você \033[31mPERDEU!\033[m')
            break
    print('Vamos jogar novamente...')
print(f'\033[31mGAME OVER!\033[m Você venceu \033[34m{v}\033[m vezes')
