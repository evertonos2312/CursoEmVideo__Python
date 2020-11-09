sexo = input('Digite seu sexo: [M/F] ').strip().upper()[0]
while sexo[0] not in "MF":
    sexo = input('Dados inválidos, por favor, informe seu sexo: ').strip().upper()
print(f'Sexo {sexo[0]} registrado com sucesso.')
