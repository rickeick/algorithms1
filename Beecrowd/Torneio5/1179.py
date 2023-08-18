par = list()
impar = list()
for i in range(15):
    N = int(input())
    if N % 2:
        impar.append(N)
        if len(impar) == 5:
            for i in range(5): print(f'impar[{i}] = {impar[i]}')
            impar = list()
    else:
        par.append(N)
        if len(par) == 5:
            for i in range(5): print(f'par[{i}] = {par[i]}')
            par = list()
i = int()
for item in impar:
    print(f'impar[{i}] = {item}')
    i += 1
i = int()
for item in par:
    print(f'par[{i}] = {item}')
    i += 1
