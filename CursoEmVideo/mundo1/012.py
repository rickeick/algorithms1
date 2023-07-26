# Calculando descontos
valor = float(input('Qual o preço do produto? R$'))
desconto = (valor * 5) / 100
total = valor - desconto
print(f'O produto que custava R${valor}, na promoção com desconto de 5% vai custar R${total:.2f}')
