# Função que calcula área
def calculaArea(largura, altura):
    return largura*altura


print('Controle de Terreno')
largura = float(input('Largura (m): '))
altura = float(input('Altura (m): '))
area = calculaArea(largura, altura)
print(f'A área de um terreno {largura}x{altura} é de {area}m²')
