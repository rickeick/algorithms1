# Estatística em produtos
import math
print(20*'=')
print('Super Economia')
print(20*'=')
total = 0
maiores_1000 = 0
menor_produto = 0
menor_preco = math.inf
while True:
    nome = input('Insira o nome do poduto: ')
    preco = float(input('Insira o preço do produto: '))
    if preco > 1000:
        maiores_1000 += 1
    if preco < menor_preco:
        menor_preco = preco
        menor_produto = nome
    total += preco
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N]: ').strip().upper()
    if resposta == 'N':
        break
print('{}RESUMO{}'.format(15*'=', 15*'='))
print(f'Total da compra: R$ {total:.2f}')
print(f'Nº produtos acima de R$ 1000: {maiores_1000}')
print(f'Produto mais barato: {menor_produto} custando R$ {menor_preco}')
