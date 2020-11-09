num = input()
if num.isnumeric():
    num = int(num)

    if num >= 0 and num <= 9999:
        und = num // 1 % 10
        dez = num // 10 % 10
        cen = num // 100 % 10
        mil = num // 1000 % 10

        print(f'Analisando o número {num}')
        print(f'Unidade: {und}')
        print(f'Dezena: {dez}')
        print(f'Centena: {cen}')
        print(f'Milhar: {mil}')
else:
    print('Digite um número valido')