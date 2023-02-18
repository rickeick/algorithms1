# Contagem regressiva
from time import sleep
print('Contagem regressiva para estourar os fogos de artifício!')
for i in range(10, -1, -1):
    sleep(1)
    if i != 0:
        print(f'{i}...')
    else:
        print('BOOOM!')
