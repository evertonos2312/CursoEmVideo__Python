nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if 7 > media >= 5:
    print('O aluno está em \033[36mRECUPERAÇÃO\033[m.')
elif media < 5:
    print('O aluno está \033[31mREPROVADO\033[m')
elif media >= 7:
    print('O aluno está \033[32mAPROVADO\033[m!')