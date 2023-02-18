# GAME: par ou ímpar
from random import randint
vezes = 0
print('='*25)
print('VAMOS JOGAR PAR OU IMPAR?')
print('='*25)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou impar [P/I]: ')).upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            vezes += 1
        else:
            print('Você Perdeu')
            break
    else:
        if total % 2 == 1:
            print('Você Venceu!')
            vezes += 1
        else:
            print('Você Perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {vezes} vezes')
