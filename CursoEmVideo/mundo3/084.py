# Lista composta e análise de dados
nomes = []
pesos = []
while True:
    nomes.append(input('Nome: '))
    pesos.append(float(input('Peso: ')))
    opcao = input('Quer continuar? [S/N]: ')
    if opcao.upper() == 'N':
        break
print()
print(f'Você cadastrou no total {len(nomes)} pessoas')
maior = max(pesos)
print(f'O maior peso foi {maior} kg. Peso de', end=' ')
for nome, peso in zip(nomes, pesos):
    if peso == maior:
        print(f'[{nome}]', end=' ')
print()
menor = min(pesos)
print(f'O menor peso foi {menor} kg. Peso de', end=' ')
for nome, peso in zip(nomes, peso):
    if peso == menor:
        print(f'[{nome}]', end=' ')
print()
