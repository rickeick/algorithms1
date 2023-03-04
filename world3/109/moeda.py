def aumentar(preco, taxa, formato=False):
    resultado = preco + (preco * taxa/100)
    return resultado if formato is False else moeda(resultado)


def diminuir(preco, taxa, formato=False):
    resultado = preco - (preco * taxa/100)
    return resultado if formato is False else moeda(resultado)

def dobro(preco, formato=False):
    resultado = preco * 2
    return resultado if formato is False else moeda(resultado)


def metade(preco, formato=False):
    resultado = preco / 2
    return resultado if formato is False else moeda(resultado)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
