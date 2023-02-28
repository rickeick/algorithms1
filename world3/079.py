# Valores únicos em uma lista
valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar!')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    opcao = input('Quer continuar? [S/N]: ')
    if opcao.upper() == 'N':
        break
print(f'Você digitou os valores {valores}')
