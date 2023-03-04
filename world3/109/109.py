# Formatando moedas em Python v2
import moeda
p = float(input('Qual o preço do produto? R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
