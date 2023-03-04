# Arquivos com Python
from lib.interface import *
from lib.arquivo import *

ARQUIVO = 'dados.txt'

if not arquivoExiste(ARQUIVO):
    criarArquivo(ARQUIVO)

while True:
    opcao = menu(['Cadastrar Pessoa', 'Listar Pessoas', 'Sair do Sistema'])
    if opcao == 1:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(ARQUIVO, nome, idade)
    elif opcao == 2:
        cabecalho('Pessoas Cadastradas')
        lerArquivo(ARQUIVO)
    elif opcao == 3:
        print('Sistema Encerrado!')
        break
    else:
        print(f'{VERMELHO}ERRO! Digite uma opção válida{FECHAR}')
