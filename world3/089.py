# Boletim com listas compostas
count = 0
nomes = []
notas = []
while True:
    nomes.append(input('Nome: '))
    notas.append(list())
    notas[count].append((float(input('Nota 1: '))))
    notas[count].append((float(input('Nota 2: '))))
    opcao = input('Quer continuar? [S/N]: ')
    if opcao.upper() == 'N':
        break
    count += 1
print()
print('Boletim da Turma:')
print('='*30)
print(f'{"Nº":<4}{"Nome":<20}{"Média":<6}')
print('='*30)
for i in range(len(nomes)):
    media = (notas[i][0] + notas[i][1]) / 2
    print(f'{i:<4}{nomes[i]:<20}{media:<6}')
print('='*30)
print()
n = 0
while n != 999:
    n = int(input('Consultar notas de qual aluno? (999 interrompe): '))
    if n != 999:
        print(f'As notas de {nomes[n]} são {notas[n]}\n')
    else:
        print('Programa finalizado!')
