# Jogo de dados em Python
from random import randint
from time import sleep
count = 1
jogos = {}
print('Valores Sorteados:')
for i in range(1, 5):
    jogos[f'Jogador{i}'] = randint(1, 6)
for jogador, valor in jogos.items():
    print(f'{jogador} tirou {valor} no dado')
    sleep(1)
print('Ranking dos Jogadores:')
jogos_ordenados = dict(sorted(jogos.items(), key=lambda item: item[1], reverse=True))
for jogador, valor in jogos_ordenados.items():
    print(f'{count}º lugar: {jogador} com {valor}.')
    count += 1
    sleep(1)
