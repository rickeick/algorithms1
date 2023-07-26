# Palpites para a mega sena
from random import randint
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(quantidade):
    jogo = []
    count = 0
    while True:
        numero = randint(1,60)
        if numero not in jogo:
            jogo.append(numero)
            count += 1
        if count == 6:
            break
    jogo.sort()
    print(f'Jogo {i+1}: {jogo}')
