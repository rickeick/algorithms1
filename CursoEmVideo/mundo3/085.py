# Listas com pares e ímpares
listas = [[],[]]
for i in range(7):
    n = int(input(f'Digite o {i+1}º valor: '))
    listas[n%2].append(n)
listas[1].sort()
print()
print(f'Os valores pares digitados foram {listas[0]}')
print(f'Os valores ímpares digitados foram {listas[1]}')
