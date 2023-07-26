from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, mode='rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, mode='wt+')
        a.close()
    except:
        return False
    else:
        return True


def lerArquivo(nome):
    try:
        a = open(nome, mode='rt')
    except:
        print(f'{VERMELHO}ERRO! Não foi possível ler o arquivo{FECHAR}')
    else:
        for linha in a:
            dados = linha.replace('\n', '').split(';')
            print(f'{dados[0]:.<33}{dados[1]:<2} anos')
        print(a.read())
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, mode='at')
    except:
        print(f'{VERMELHO}ERRO! Não foi possível ler o arquivo{FECHAR}')
    else:
        a.write(f'{nome};{idade}\n')
        print(f'Novo registro de {nome} adicionado!')
        a.close()
