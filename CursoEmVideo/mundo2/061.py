# Progressão aritmética v2.0
titulo = 'Gerador de PA v2.0'
print('-=' * 20)
print('{:^40}'.format(titulo))
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
