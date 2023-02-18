# Sequência de Fibonacci
anterior = 1
fibonacci = 0
n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))
while n != 0:
    print(fibonacci, end=' → ')
    fibonacci = fibonacci + anterior
    anterior = fibonacci - anterior
    n -= 1
print('FIM')
