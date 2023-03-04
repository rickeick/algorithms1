# Exercitando módulos em Python
import moeda
p = float(input('Qual o preço do produto? R$'))
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
