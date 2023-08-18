A = list()
for i in range(100):
    n = float(input())
    A.append(n)
    if n <= 10:
        print(f'A[{i}] = {A[i]}')
