# Número por extenso
numeros = (
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'catorze',
    'quinze',
    'dezeseis',
    'dezesete',
    'dezoito',
    'dezenove',
    'vinte'
)
n = int(input('Digite um número entre 0 e 20: '))
while n not in range(0, 20):
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[n]}')
