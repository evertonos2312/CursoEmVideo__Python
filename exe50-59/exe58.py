from random import randint
from time import sleep
cpu = randint(0, 10)
print('-=-' * 22)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar =)')
print('-=-' * 22)
sleep(1)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    print('PROCESSANDO...')
    sleep(0.5)
    print()
    palpites += 1
    if jogador == cpu:
        acertou = True
    else:
        if jogador < cpu:
            print('Mais...Tente mais uma vez.')
        else:
            print('Menos...Tente mais uma vez.')

print(f'PARABÉNS! Você acertou com \033[32m{palpites}\033[m tentativas')
