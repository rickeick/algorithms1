def leiaDinheiro(prompt=''):
    valido = False
    while not valido:
        valor = str(input(prompt).strip().replace(',', '.'))
        if valor.isalpha() or valor == '':
            print(f'ERRO! \"{valor}\" não é um preço válido')
        else:
            valido = True
    return float(valor)
