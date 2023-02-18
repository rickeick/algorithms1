# Analisando triângulos
A = float(input('Comprimento do Primeiro segmento: '))
B = float(input('Comprimento do Segundo segmento: '))
C = float(input('Comprimento do Terceiro segmento: '))
if (A + B > C) or (A + C > B) or (C + B > A):
    print('Estes segementos PODEM CRIAR um triângulo!')
else:
    print('Estes segementos NÃO PODEM CRIAR um triângulo!')
