# Custo da viagem
distancia = float(input('Qual a distância da sua viagem? '))
print(f'Você estar preste a começar um viagem de {distancia}km')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'O preço da sua passagem será de R${preco}')
