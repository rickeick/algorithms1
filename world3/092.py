# Cadastro de trabalhador em Python
from datetime import date
dados = {}
atual = date.today().year
dados['Nome'] = input('Nome: ')
nascimento = int(input('Ano de Nascimento: '))
dados['Idade'] = atual - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho [0 não tem]: '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = input('Salário: R$')
    dados['Aposentadoria'] = dados['Contratação'] + 35 - nascimento
    print('\nDados:')
    for chave, valor in dados.items():
        print(f'{chave} tem o valor {valor}')
else:
    print('\nDados:')
    for chave, valor in dados.items():
        print(f'{chave} tem o valor {valor}')
