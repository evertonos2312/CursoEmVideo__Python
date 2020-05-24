print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[32mPODEM\033[m formar um triângulo do tipo:', end=' ')
    if r1 == r2 == r3:
        print('\033[32mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[32mESCALENO\033[m')
    else:
        print('\033[32mISÓSCELES\033[m')

else:
    print('Os segmentos acima \033[31mNÃO\033[m podem formar um triângulo')
