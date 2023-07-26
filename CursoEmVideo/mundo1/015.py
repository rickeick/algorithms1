# Aluguel de carros
dias = int(input('Quantos dias o carro foi alugado? '))
distancia = float(input('Quantos Km foi pecorrido? '))
total = (dias*60)+(distancia*0.15)
print(f'O total a pagar é R${total:.2f}')
