# Tuplas com times de futebol
classificacao = (
    'Palmeiras',
    'Internacional',
    'Fluminense',
    'Corinthians',
    'Flamengo',
    'Atlético-PR',
    'Atlético-MG',
    'Fortaleza',
    'São Paulo',
    'América-MG',
    'Botafogo',
    'Santos',
    'Goiás',
    'Bragantino',
    'Curitiba',
    'Cuiabá',
    'Ceára SC',
    'Atlético-GO',
    'Avaí',
    'Juventude'
)
print('Os 5 primeiros colocados são:')
for time in classificacao[:5]:
    print(time)
print()
print('Os 4 últimos colocados são:')
for time in classificacao[15:]:
    print(time)
print()
print('Times em ordem alfabética:')
for time in sorted(classificacao):
    print(time)
print()
posicao = classificacao.index('Flamengo') + 1
print(f'O Flamengo está em {posicao}º lugar')
