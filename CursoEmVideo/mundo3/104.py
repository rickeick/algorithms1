# Validando entrada de dados em Python
def leiaInt(promt=''):
    valor = str(input(promt))
    while not valor.isnumeric():
        print('ERRO! Digite um número inteiro válido!')
        valor = str(input(promt))
    return int(valor)


n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')
