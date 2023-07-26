# Analisador de triângulos v2.0
print('Analisador de Triângulos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
triangulo = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
equilatero = (r1 == r2) and (r3 == r1)
isoceles = (r1 == r2) and (r3 != r1) and (r3 != r2) or (r3 == r2) and (r3 != r1) or (r1 == r3) and (r1 != r2)
escaleno = (r1 != r2) and (r3 != r1)
if triangulo and equilatero:
    print('Podem formar um triângulo equilátero')
elif triangulo and isoceles:
    print('Podem formar um triângulo isóceles')
elif triangulo and escaleno:
    print('Podem formar um triângulo escaleno')
else:
    print('Não podem formar um triângulo.')
