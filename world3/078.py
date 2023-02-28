# Maior e menor valores na lista
valores = []
for i in range(5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
print(f'Os valores digitados foram {valores}')
maior = max(valores)
print(f'O maior valor foi o {maior} digitado nas posições:', end=' ')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(indice, end=' ')
print()
menor = min(valores)
print(f'O maior valor foi o {menor} digitado nas posições:', end=' ')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(indice, end=' ')
print()
