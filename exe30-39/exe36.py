vcasa = float(input('Digite o valor da casa: R$'))
salario = float(input('DIgite seu salário: R$'))
anos = int(input('Em quantos anos quer pagar?'))
emprestimo = vcasa / (anos * 12)

print(f'Para pegar uma casa de R${vcasa:.2f} em {anos} anos a prestação será de R${emprestimo:.2f}')
if emprestimo <= (salario * 0.30):
    print('Emprestimo pode ser \033[32mCONCEDIDO\033[m!')
else:
    print('Emprestimo \033[31mnNEGADO\033[m!')
