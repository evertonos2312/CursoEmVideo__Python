from time import sleep
num = int(input('Digite um número: '))
print('Qual será a base de conversão?')
sleep(0.2)
print('-=' * 20)
print('[ \033[32m1\033[m ] converter para \033[31mBINÁRIO\033[m')
print('[ \033[32m2\033[m ] converter para \033[31mOCTAL\033[m')
print('[ \033[32m3\033[m ] converter para \033[31mHEXADECIMAL\033[m')
print('-=' * 20)

base = int(input('Sua opção: '))
print()
print('PROCESSANDO...')
sleep(1)
print()

if base == 1:
    print(f'Convertendo {num} para BINÀRIO: {bin(num)[2:]}')
elif base == 2:
    print(f'Convertendo {num} para OCTAL: {oct(num)[2:]}')
elif base == 3:
    print(f'Convertendo {num} para HEXADECIMAL: {hex(num)[2:]}')
else:
    print('Digite um número de 1 a 3')
