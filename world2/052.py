# Números primos
primo = True
n = int(input('Digite um número: '))
if n < 2:
    primo = False
else:
    for c in range(2, n-1):
        if n % c == 0:
            primo = False
            break
if primo:
    print(f'{n} é um número primo!')
else:
    print(f'{n} não é um número primo!')
