# Alistamento militar
from datetime import date
atual = date.today().year
nascimento = int(input('Qual o seu ano de nascimento? '))
idade = atual - nascimento
if idade == 18:
    print('Corra para se alistar já!')
elif idade < 18:
    falta = 18 - idade
    ano = atual + falta
    print(f'Falta {falta} anos para você se alistar, compareça para o alistamento no ano de {ano}')
else:
    ano = atual - (idade - 18)
    print(f'Você ja passou da idade de se alistar, deveria ter se alistado em {ano}')
