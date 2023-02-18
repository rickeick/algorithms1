# Simulador de caixa eletrônico
valor = int(input('Informe o valor a ser sacado : '))
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f'Notas de 50 = {nota50}')
print(f'Notas de 20 = {nota20}')
print(f'Notas de 10 = {nota10}')
print(f'Notas de 1 = {nota1}')
