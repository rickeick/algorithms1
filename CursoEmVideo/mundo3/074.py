# Maior e menor valores em tupla
from random import randint
numeros = (
    randint(1,10),
    randint(1,10),
    randint(1,10),
    randint(1,10),
    randint(1,10)
)
print('Os números sorteados foram:', end=' ')
for n in numeros:
    print(n, end=' ')
print()
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
