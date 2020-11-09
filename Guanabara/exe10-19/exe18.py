import math
ang = float(input('Digite o ângulo desejado: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print(f'O ângulo de {ang:.2f} tem o SENO de {sen:.2f}, o COS de {cos:.2f} e a TAN de {tg:.2f}')
