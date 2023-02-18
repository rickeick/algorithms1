# Tabuada v3.0
n = int(input('Digite um número para ver sua tabuada: '))
while n != 0:
    print('='*14)
    for i in range(0, 11):
        print(f'{n} X {i} = {n*i}')
    print('='*14)
    n = int(input('Digite um número para ver sua tabuada: '))
print('FIM DO PROGRAMA')
