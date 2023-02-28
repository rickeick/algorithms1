# Matriz em Python
matriz = [[],[],[]]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para posição [{i},{j}]: ')))
print()
print('Matriz:')
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^3}]', end='')
    print()
