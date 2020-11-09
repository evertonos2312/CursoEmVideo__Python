times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print('Qual opção deseja?:')
print('\n[1] Os 5 primeiros'
      '\n[2] Os últimos 4 colocados'
      '\n[3] Times em ordem alfabética'
      '\n[4] Em que posição o Chapecoense está'
      '\n[5] Sair')
print('-=' * 15)
while True:
    escolha = int(input('Digite a opção desejada: '))
    if escolha == 1:
        print(f'Os 5 primeiros colocados são: ')
        for x in range(0, 5):
            print(times[x])
    if escolha == 2:
        print(f'Os 4 últimos colocados são:')
        for k in range(4):
            print(times[-4 + k])
    if escolha == 3:
        print('Times em ordem alfabética:')
        temp = sorted(times)
        for x in range(len(times)):
            print(temp[x])
        print()
    if escolha == 4:
        print(f'Chapecoense está na {times.index("Chapecoense")+ 1}° posição')
        print()
    if escolha == 5:
        break
