# Função para votação
from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos! Não Vota'
    elif 16 < idade <= 18 or idade >= 65:
        return f'Com {idade} anos! Voto Opcional'
    else:
        return f'Com {idade} anos! Voto Obrigatório'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
