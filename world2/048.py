# Soma dos ímpares multiplos de 3
sum = 0
print('Todos os números ímpares que são múltiplos de 3 e estão entre 1 e 500:')
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i, end=' ')
        sum += i
print(f'\nSOMA DE TODOS: {sum}')
