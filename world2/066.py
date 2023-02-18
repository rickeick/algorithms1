# Vários números com flag
n = 0
sum = 0
count = 0
while n != 999:
    n = int(input('Digite um número inteiro ou 999 para parar: '))
    if n != 999:
        sum += n
        count += 1
print(f'Foram digitados {count} números e a soma entre eles foi {sum}')
