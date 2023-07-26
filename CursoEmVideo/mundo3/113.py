# Funções aprofundadas em Python
def leiaInt(promt=''):
    while True:
        try:
            valor = int(input(promt))
            return valor
        except KeyboardInterrupt:
            print('\nUsuário preferiu não digitar esse número')
            return 0
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido!')


def leiaFloat(promt=''):
    while True:
        try:
            valor = int(input(promt))
            return valor
        except KeyboardInterrupt:
            print('\nUsuário preferiu não digitar esse número')
            return 0
        except (ValueError, TypeError):
            print('ERRO! Digite um número decimal válido!')


inteiro = leiaInt('Digite um número inteiro: ')
decimal = leiaFloat('Digite um número decimal: ')
print(f'O número inteiro digitado foi {inteiro} e o decimal foi {decimal}')
