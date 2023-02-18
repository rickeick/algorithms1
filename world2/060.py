# Cálculo do fatorial
fat = 1
n = int(input('Digite um número para saber o seu fatorial: '))
print(f'{n}! = ', end='')
while n != 0:
    print(n, end='')
    fat *= n; n -= 1
    print(' x ' if n > 0 else '', end='')
print(f' = {fat}')
