from random import randint
from time import sleep
cpu = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar =)')
print('-=-' * 20)

player = input('Em que número eu pensei? ')
print('PROCESSANDO...')
sleep(2)

if player.isdigit():
    player = int(player)

    if player == cpu:
        print('PARABÉNS! Você venceu!')
    else:
        print(f'VOCÊ PERDEU! Eu pensei no número {cpu} e não no número {player}')
else:
    print('Isso não vale!!')
