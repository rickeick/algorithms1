# Procurando uma string dentro da outra
nome = str(input('Qual seu nome completo? '))
print('Seu nome tem Silva?', end=' ')
print(nome.find('Silva') > 0)
