# Conversor de bases numéricas
n = int(input('Digite um número inteiro: '))
A = bin(n)
B = oct(n)
C = hex(n)
print('ESCOLHA A FORMA DE CONVERSÃO')
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
opcao = int(input('Opção: '))
if opcao == 1:
    print(f'O número em forma binária é {A}!')
elif opcao == 2:
    print(f'O número em octal é {B}!')
elif opcao == 3:
    print(f'O número em forma hexadecimal é {C}!')
else:
    print('Opção Inválida')
