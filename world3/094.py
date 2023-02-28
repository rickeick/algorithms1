# Unindo dicionários e listas
pessoa = {}
pessoas = []
while True:
    pessoa['Nome'] = input('Nome: ')
    sexo = input('Sexo[M/F]: ').upper()
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        sexo = input('Sexo[M/F]: ').upper()
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(input('Idade: '))
    opcao = input('Quer Continuar? [S/N]: ')
    while opcao not in 'SsNn':
        print('ERRO! Por favor, responda apenas S ou N')
        opcao = input('Quer Continuar? [S/N]: ')
    pessoas.append(pessoa.copy())
    if opcao in 'Nn':
        break
print()
total = 0
quantidade = len(pessoas)
for i, pessoa in enumerate(pessoas):
    total += pessoa['Idade']
media = total/quantidade
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A média de idade é de {media} anos')
print(f'C) As mulheres cadastradas foram', end=' ')
for pessoa in pessoas:
    if pessoa['Sexo'] == 'F':
        print(pessoa['Nome'], end=' ')
print('\nD) Lista de pessoas que estão acima da média:')
for pessoa in pessoas:
    if pessoa['Idade'] >= media:
        print(end='    ')
        for chave, valor in pessoa.items():
            print(f'{chave} = {valor}', end='; ')
        print()
