# Mais sobre matriz em Python
pares = 0
coluna = 0
matriz = [[],[],[]]
for i in range(3):
    for j in range(3):
        n = int(input(f'Digite um valor para posição [{i},{j}]: '))
        if n % 2 == 0:
            pares += n
        if j == 2:
            coluna += n
        matriz[i].append(n)
print()
print('Matriz:')
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^3}]', end='')
    print()
print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
