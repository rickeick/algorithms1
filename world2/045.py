# GAME: pedra, papel e tesoura
from random import choice
opcoes = ['pedra', 'papel', 'tesoura']
computador = choice(opcoes)
print('Digite qual você quer jogar!')
jogador = str(input('PEDRA, PAPEL ou TESOURA? ')).lower().strip()
if jogador in opcoes:
    print(f'Você jogou {jogador.upper()} e eu joguei {computador.upper()}')
    if computador == jogador:
        print('Nós empatamos!')
    elif computador == 'pedra' and jogador == 'papel':
        print('Você ganhou!')
    elif computador == 'pedra' and jogador == 'tesoura':
        print('Eu ganhei!')
    elif computador == 'papel' and jogador == 'pedra':
        print('Eu ganhei!')
    elif computador == 'papel' and jogador == 'tesoura':
        print('Você ganhou!')
    elif computador == 'tesoura' and jogador == 'pedra':
        print('Você ganhou!')
    elif computador == 'tesoura' and jogador == 'papel':
        print('Eu ganhei!')
    else:
        print('Erro!')
