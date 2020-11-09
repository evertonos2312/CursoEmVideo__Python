print('-=' * 20)
print(f'{" LOJAS SILVA ":=^40}')
print('-=' * 20)
print()
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
total = 0
if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opcao == 4:
    total = preco + (preco * 0.20)
    tparcela = int(input('Quantas parcelas? '))
    parcela = total / tparcela
    print(f'Sua compra será parcelada em {tparcela}x R${parcela:.2f} COM JUROS')
else:
    total = preco
    print('\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
