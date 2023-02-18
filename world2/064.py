# Tratando vários valores
n = 0
sum = 0
cont = 0
while n != 999:
    n = int(input('Digite um número inteiro ou 999 para parar: '))
    if n != 999:
        sum += n
        cont += 1
print(f'Foram digitados {cont} números e a soma entre eles foi {sum}')
