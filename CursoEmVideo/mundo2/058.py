# Jogo da advinhação v3.0
from random import randint
from time import sleep
print('Vamos Jogar um jogo? Vou pensar num número de 0 a 5')
sleep(3)
print('Você tem 5 tentativas!')
print('A cada erro você perde um ponto!')
print('Se você chegar a 0 pontos você perde!')
sleep(3)
tentativa = 0
pontuacao = 10
resposta = randint(0, 5)
print(resposta)
numero = int(input('Escolha um número de 0 a 5: '))
print('Processando...')
sleep(1)
while not numero == resposta:
    tentativa += 1
    if numero > resposta:
        numero = int(input('Errou! Tente um número menor!: '))
    elif numero < resposta:
        numero = int(input('Errou! Tente um número maior!: '))
    print('Processando...')
    pontuacao -= 2
    sleep(1)
    if tentativa == 4:
        print(f'GAME OVER! O computador escolheu o número {resposta}')
if pontuacao >= 0:
    print(f'Acertou! O computador escolheu o número {resposta}')
    print(f'Você fez um total de {pontuacao} pontos')
