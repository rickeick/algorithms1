# Dividindo valores em várias listas
pares = []
impares = []
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = input('Quer continuar? [S/N]: ')
    if opcao.upper() == 'N':
        break
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print()
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
