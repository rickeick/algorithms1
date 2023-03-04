# Sistema interativo de ajuda em Python
def titulo(mensagem):
    tamanho = len(mensagem) + 4
    print('~'*tamanho)
    print(f'  {mensagem}')
    print('~'*tamanho)


def ajuda(comando):
    help(comando)


while True:
    titulo('Sistema de Ajuda PyHelp')
    comando = str(input('Nome da função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    ajuda(comando)
