# Ficha do Jogador
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')

n = str(input('Nome do Jogador: ').strip())
g = str(input('Números de Gols: ').strip())
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
