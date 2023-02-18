# Super progressão aritmética v3.0
titulo = 'Gerador de PA v3.0'
print('-=' * 20)
print('{:^40}'.format(titulo))
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
mais = 11
while cont < mais:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
    if cont > mais-1:
        print('Pause')
        mais = int(input('Quantos termos você quer mostra a mais? '))
        mais += cont
    elif cont == 11:
        cont += 1
cont -= 1
print('Progressão foi finalizada com {} termos mostrados'.format(cont))
