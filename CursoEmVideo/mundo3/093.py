# Cadastro de jogador de futebol
jogador = {}
jogador['Nome'] = input('Nome do Jogador: ')
n = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
jogador['Gols'] = []
jogador['Total'] = 0
for i in range(n):
    gols = int(input(f'Quantos gols na partida {i}? '))
    jogador['Gols'].append(gols)
    jogador['Total'] += gols
print(f'\n{jogador}\n')
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print()
print(f'O jogador {jogador["Nome"]} jogou {n} partidas:')
for indice, valor in enumerate(jogador['Gols']):
    print(f'    Na partida {indice}, fez {valor} gols')
print(f'Foi um total de {jogador["Total"]} gols')
