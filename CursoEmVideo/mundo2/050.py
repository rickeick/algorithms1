# Soma dos pares
sum = 0
count = 0
for i in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        count += 1
        sum += n
if count == 0:
    print('Você não digitou nenhum número par, portanto, o seu total é 0.')
elif count == 1:
    print(f'Você digitou {count} número par. O seu total é {sum}.')
else:
    print(f'Você digitou {count} números pares. A soma total deles é {sum}.')
