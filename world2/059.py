# Criando um menu de opções
from time import sleep
v = 0
n1 = 0
n2 = 0
opcao = '4'
while v != 5:
    while opcao == '4':
        opcao = ''
        n1 = int(input('Digite Um Valor: '))
        n2 = int(input('Digite Outro Valor: '))
    print()
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair Do Programa')
    opcao = str(input('Digite uma opção: '))
    if opcao == '1':
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif opcao == '2':
        print(f'O produto entre {n1} e {n2} é {n1*n2}')
    elif opcao == '3':
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n1 == n2:
            print(f'Os números são iguais')
        else:
            print(f'{n2} é maior que {n1}')
    elif opcao == '4':
        print('Escolha os novos números')
    elif opcao == '5':
        v = 5
        print('Programa Encerrado!')
    else:
        print('Opção inválida, tente novamente!')
