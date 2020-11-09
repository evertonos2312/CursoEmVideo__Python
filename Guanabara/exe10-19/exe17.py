co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (co ** 2 + ca * 22) ** (1 / 2)
print(f'A hipotenusa de CO {co} e CA {ca} é {hip:.2f}')
