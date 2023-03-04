# Função de Contador
from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if (i > f) and (p > 0):
        intervalo = range(i, f-1, -p)
    elif (i > f) and (p < 0):
        intervalo = range(i, f-1, p)
    else:
        intervalo = range(i, f+1, p)
    for count in intervalo:
        print(count, end=' ', flush=True); sleep(0.5)
    print('FIM\n')

contador(1, 10, 1)
contador(10, 0, 2)
contador(20, 0, -4)
contador(12, -10, 7)
