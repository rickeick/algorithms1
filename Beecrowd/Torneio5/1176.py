def fibonacci(n):
    lista = list()
    fib, aux = 0, 1
    while n != 0:
        lista.append(fib)
        fib = fib + aux
        aux = fib - aux
        n -= 1
    return lista


T = int(input())
for i in range(T):
    n = int(input())
    valor = fibonacci(100)[n]
    print(f'Fib({n}) = {valor}')
