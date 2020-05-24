cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print(f'Tente novamente. ', end='')
    print(f'Você digitou o número {cont[num]}')
    escolha = input('Você quer continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
