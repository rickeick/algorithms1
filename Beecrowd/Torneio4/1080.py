maior = int()
posicao = int()
for i in range(1, 101):
    x = int(input())
    if x > maior:
        maior = x
        posicao = i
print(maior)
print(posicao)
