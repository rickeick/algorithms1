AZUL = '\033[34m'
AMARELO = '\033[33m'
VERMELHO = '\033[31m'
FECHAR = '\033[m'

def linha(tam=40):
    return '='*tam


def cabecalho(texto):
    print(linha())
    print(texto.center(40))
    print(linha())


def leiaInt(promt=''):
    while True:
        try:
            valor = int(input(promt))
            return valor
        except KeyboardInterrupt:
            print(f'\n{VERMELHO}Usuário preferiu não digitar esse número{FECHAR}')
            return 0
        except (ValueError, TypeError):
            print(f'{VERMELHO}ERRO! Digite um número inteiro válido!{FECHAR}')


def menu(lista):
    cabecalho('Menu Principal')
    for index, item in enumerate(lista, start=1):
        print(f'{AMARELO}{index}{FECHAR} - {AZUL}{item}{FECHAR}')
    print(linha())
    opcao = leiaInt(f'{AMARELO}Digite uma Opção: {FECHAR}')
    return opcao
