from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print(f'O atleta tem {idade} anos e está na categoria: \033[36mMIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e está na categoria: \033[36mINFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos e está na categoria: \033[36mJUNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e está na categoria: \033[36mSÊNIOR')
else:
    print(f'O atleta tem {idade} anos e está na categoria: \033[36mMASTER')
