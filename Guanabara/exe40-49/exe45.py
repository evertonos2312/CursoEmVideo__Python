from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Computador escolheu \033[32m{itens[cpu]}\033[m')
print(f'Jogador escolheu \033[32m{itens[jogador]}\033[m')
print('-=' * 11)
if cpu == 0:
    if jogador == 0:
        print('\033[1;33mVOCÊS EMPATARAM\033[m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;36mCOMPUTADOR VENCEU!\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif cpu == 1:
    if jogador == 0:
        print('\033[1;36mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[1;33mVOCÊS EMPATARAM\033[m')
    elif jogador == 2:
        print('\033[1;32mJOGADOR VENCEU!\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif cpu == 2:
    if jogador == 0:
        print('\033[1;32mJOGADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[1;36mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;33mVOCÊS EMPATARAM\033[m')
    else:
        print('JOGADA INVÁLIDA')
