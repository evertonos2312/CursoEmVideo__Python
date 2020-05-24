real = input('Quanto dinheiro você tem  na carteira? R$ ')
if real.isdecimal():
    real = float(real)
dolar = real / 5.20
euro = real / 5.68
iene = real / 0.048
print(f'Com R$ {real:.2f} você pode comprar US$ {dolar:.2f}')
print()
print(f'Com R$ {real:.2f} você pode comprar € {euro:.2f}')
print()
print(f'Com R$ {real:.2f} você pode comprar ¥ {iene:.2f}')

