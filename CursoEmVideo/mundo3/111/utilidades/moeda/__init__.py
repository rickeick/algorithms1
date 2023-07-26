def aumentar(preco, taxa, formato=False):
    ret = preco + (preco * taxa/100)
    return ret if formato is False else moeda(ret)


def diminuir(preco, taxa, formato=False):
    ret = preco - (preco * taxa/100)
    return ret if formato is False else moeda(ret)

def dobro(preco, formato=False):
    ret = preco * 2
    return ret if formato is False else moeda(ret)


def metade(preco, formato=False):
    ret = preco / 2
    return ret if formato is False else moeda(ret)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco, aumento, reducao):
    print('='*30)
    print(f'{"Resumo do Preço":^30}')
    print('='*30)
    print(f'Preço Analisado:{moeda(preco):>13}')
    print(f'Dobro do Preço:{dobro(preco, True):>14}')
    print(f'Metade do Preço:{metade(preco, True):>13}')
    print(f'{aumento}% de aumento:{aumentar(preco, aumento, True):>14}')
    print(f'{reducao}% de redução:{diminuir(preco, aumento, True):>14}')
    print('='*30)
