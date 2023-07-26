# Funções para sortear e somar
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(5):
        n = randint(1, 10)
        print(n, end=' ', flush=True); sleep(0.5)
        lista.append(n)
    print('Pronto!')


def somaPares(lista):
    total = 0
    for valor in lista:
        if valor % 2 == 0:
            total += valor
    print(f'Somando os valores pares da lista {lista}, temos {total}')


numeros = list()
sorteia(numeros)
somaPares(numeros)
