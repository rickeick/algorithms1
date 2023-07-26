# Grupo da maioridade
from datetime import date
countMaior = 0
countMenor = 0
atual = date.today().year
for i in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {i}º pessoa: '))
    if (atual - nascimento) >= 18:
        countMaior += 1
    else:
        countMenor += 1
print('Nesse grupo de pessoas há:')
print(f'{countMaior} pessoas maiores de idade')
print(f'{countMenor} pessoas menores de idade')
