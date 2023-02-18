# Índice de massa corporal
peso = float(input('Digite seu peso Kg: '))
altura = float(input('Digite sua altura m: '))
imc = peso / (altura ** 2)
print(f'Você está com uma massa corporal de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo da média de peso.')
elif imc <= 25:
    print('Você está no peso idal')
elif imc < 30:
    print('Você está com um nível de sobrepeso.')
elif imc <= 40:
    print('Você está com um nível de obesidade.')
else:
    print('Você está com um nível de obesidade mórbida.')
