# Função que descobre o maior
from time import sleep

def maior(*args):
    if len(args) != 0:
        maior = args[0]
        print('Analisando os valores passados:', end=' ')
        for valor in args:
            print(valor, end=' ', flush=True); sleep(0.5)
            if maior < valor:
                maior = valor
        print(f'\nForam informados ao todo {len(args)} valores'); sleep(1)
        print(f'O maior valor informado foi {maior}\n'); sleep(1)
    else:
        print('Nenhum valor foi passado')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
