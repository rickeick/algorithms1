# Extraindo dados de uma lista
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = input('Quer continuar? [S/N]: ')
    if opcao.upper() == 'N':
        break
print()
print(f'Você digitou {len(valores)} valores')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O valor 5 foi encontrado na lista')
else:
    print('O Valor 5 não foi encontrado na lista')
