# Sorteando uma ordem na lista
from random import shuffle
aluno1 = input('Nome do 1ª aluno: ')
aluno2 = input('Nome do 2ª aluno: ')
aluno3 = input('Nome do 3ª aluno: ')
aluno4 = input('Nome do 4ª aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
