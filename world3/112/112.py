# Entrada de dados monetários
from utilidades import dado
from utilidades import moeda

p = dado.leiaDinheiro('Qual o preço do produto? R$')
moeda.resumo(p, 10, 10)
