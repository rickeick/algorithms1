# Maior e menor valores
sum = 0
maior = 0
menor = 0
count = 0
opcao = True
while opcao:
    n = float(input('Digite um número: '))
    if count == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    count += 1
    sum += n
    c = input('Quer continuar? [S/N] ').strip().upper()[0]
    while c != 'S' and c != 'N':
        c = input('Opção inválida, favor tentar novamente: [S/N] ').strip().upper()[0]
    if c == 'S':
        opcao = True
    else:
        opcao = False
print(f'Você digitou {sum} números com média {sum/count:.1f}')
print(f'O maior foi {maior} e o menor foi {menor}')
