num = input('Digite um número: ')
if num.isdigit():
    num = int(num)

    print('Número par' if num % 2 == 0 else 'Número impar')
