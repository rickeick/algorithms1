# Jogo da advinhação
from time import sleep
from random import randint
computador = randint(0, 5)
print('Vou penser em um número de 0 a 5. Tente Advinhar!')
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if computador == jogador:
    print('PARABÉNS! Você conseguiu acertar!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
