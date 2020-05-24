num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'\n\033[mO número \033[32m{num}\033[m foi divisível \033[32m{tot}\033[m vezes. ')
if tot == 2:
    print('E por isso ele é \033[32mPRIMO\033[m')
else:
    print('E por isso ele \033[31mNÃ0\033[m é PRIMO')
