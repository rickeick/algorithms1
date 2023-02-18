# Comparando números
from time import sleep
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
print('Calculando a resposta...')
sleep(1.5)
if primeiro > segundo:
    print('O maior número é {primeiro}')
    print('E menor número é {segundo}')
elif segundo > primeiro:
    print('O maior número é {segundo} ')
    print('E menor número é {primeiro}')
else:
    print('Os números são iguais.')
