# Lista ordenada sem repetições
valores = []
for i in range(5):
    n = int(input('Digite um número: '))
    if (i == 0) or (n > valores[-1]):
        print(f'Valor adicionado no final da lista')
        valores.append(n)
    else:
        posicao = 0
        while posicao < len(valores):
            if n <= valores[posicao]:
                print(f'Valor adicionado na posição {posicao} da lista')
                valores.insert(posicao, n)
                break
            posicao += 1
print(f'Os valores digitados em ordem foram {valores}')
