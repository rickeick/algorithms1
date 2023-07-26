# Aprimorando os dicionários
time = []
opcao = 'S'
while opcao != 'N':
    jogador = {}
    jogador['Nome'] = input('Nome do Jogador: ')
    n = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Gols'] = []
    jogador['Total'] = 0
    for i in range(n):
        gols = int(input(f'    Quantos gols na partida {i+1}? '))
        jogador['Gols'].append(gols)
        jogador['Total'] += gols
    time.append(jogador.copy())
    opcao = input('Quer continuar? [S/N]: ').upper()
print()
print('='*40)
print(f'{"Cod":<4}{"Nome":<14}{"Gols":<17}{"Total":<5}')
print('='*40)
for indice, jogador in enumerate(time):
    nome = jogador['Nome']
    total = jogador['Total']
    gols = str(jogador['Gols'])
    print(f'{indice:>3} {nome:<14}{gols:<17}{total:<5}')
print('='*40)
n = 0
while n != 999:
    n = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if n < len(time):
        nome = time[n]['Nome']
        gols = time[n]['Gols']
        print(f'Levantamento do jogador {nome}:')
        for indice, gol in enumerate(gols):
            print(f'    No jogo {i+1}, fez {gol} gols')
    elif n != 999:
        print(f'ERRO! não existe jogador com código {n}')
    else:
        print('Programa finalizado!')
