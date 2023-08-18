quant = int(input())
contin = int()
contout = int()
for i in range(quant):
    X = int(input())
    if 10 <= X <= 20: contin += 1
    else: contout += 1
print(f'{contin} in')
print(f'{contout} out')
