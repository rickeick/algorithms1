# Função para Fatorial
def fatorial(n, show=False):
    """
    Calcula o fatorial de um número
    param n: número para ser usado no cálculo
    param show: (opcional) mostra ou não a conta
    return: o valor do fatorial do número n
    """
    fat = 1
    string = str()
    string += f'{n}! = '
    while n != 0:
        string += str(n)
        fat *= n; n -= 1
        string += ' x ' if n > 0 else ''
    string += f' = {fat}'
    if show:
        return string
    else:
        return fat

print(fatorial(10, show=True))
