# Pintando parede
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede:'))
area = largura * altura
litro = area / 2
print(f'Sua parede tem dimensão de {largura}x{altura} e sua área é de {area}')
print(f'Para pintar essa parede, você presisará de {litro}l de tintas')
