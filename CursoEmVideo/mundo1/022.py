# Analisador de nomes
from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(3)
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
total = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {total} letras')
print(f'Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras')
