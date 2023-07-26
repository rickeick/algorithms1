# Classificando atletas
from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos!')
if idade in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
    print('Classificação MIRIM')
elif idade in (10, 11, 12, 13, 14):
    print('Classificação INFANTIL')
elif idade in (15, 16, 17, 18, 19):
    print('Classificação JÚNIOR')
elif idade in (20, 21, 22, 23, 24, 25):
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')
