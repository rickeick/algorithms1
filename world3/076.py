# Lista de preços com tuplas
dados = (
    'Lápis', 1.75,
    'Borracha', 2.0,
    'Caderno', 15.9,
    'Estojo', 25.0,
    'Transferidor', 4.2,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.3,
    'Livro', 34.9
)
print('='*40)
print(f'{"Listagem de Preços":^40}')
print('='*40)
for indice in range(len(dados)):
    if indice % 2 == 0:
        print(f'{dados[indice]:-<31}', end='')
    elif indice % 2 == 1:
        print(f'R$ {dados[indice]:>6.2f}')
print('='*40)
