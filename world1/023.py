# Separando dígitos de um número
n = int(input('Informe um número de quatro digitos: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Analisando o número {m}')
print(f'Unidades: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Unidades de milhar: {m}')
