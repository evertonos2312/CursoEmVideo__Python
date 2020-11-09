print("=================================================================")
print("=====================CALCULO DE IMC==============================")
print("=================================================================")

nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
nascimento = int(2020)

imc = (peso / (altura ** 2))

print("=================================================================")

print(f'\033[32m{nome}\033[m tem \033[32m{idade}\033[m anos, \033[32m{altura}\033[m '
      f'de altura e pesa \033[32m{peso}\033[m kg')
print(f'O IMC de \033[32m{nome}\033[m é de \033[32m{imc:.2f}\033[m.')
print(f'\033[32m{nome}\033[m nasceu em \033[32m{nascimento - idade}\033[m.')

if imc <= 18.5:
    print("Você está abaixo do peso")
elif imc <= 24.9:
    print("Seu peso está normal")
elif imc <= 29.9:
    print("Você está com sobrepeso")
elif imc <= 34.9:
    print("Você está com obesidade grau 1")
elif imc <= 39.9:
    print("Você está com obesidade grau 2")
elif imc >= 40:
    print("Você está com obesidade grau 3")
