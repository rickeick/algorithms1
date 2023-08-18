X = float(input())
N = [X]
for i in range(99): N.append(N[i]/2)
for i in range(100): print(f'N[{i}] = {N[i]:.4f}')
