X = list()
for i in range(10):
    n = int(input())
    if n < 1: n = 1
    X.append(n)
    print(f'X[{i}] = {X[i]}')
