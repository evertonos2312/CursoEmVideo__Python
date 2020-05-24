num = []

while len(num) < 3:
    n = int(input())
    num.append(n)

print(f'O menor valor é {min(num)}')
print(f'O maior valor é {max(num)}')
print(f'A lista é: {num}')
