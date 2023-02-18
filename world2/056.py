# Analisador completo
cont = 0
maior = 0
media = 0
homem = ''
for i in range(1, 5):
    print(f'-----{i}º PESSOA-----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    media += idade
    if sexo == 'M':
        if maior < idade:
            maior = idade
            homem = nome
    if sexo == 'F' and idade < 20:
        cont += 1
media /= 4
print('-----Resultado-----')
print(f'A média das idades é {media}')
print(f'O homem mais velho tem {maior} anos e se chama {homem}')
print(f'Ao todo tem {cont} mulher(es) com menos de 20 anos')
