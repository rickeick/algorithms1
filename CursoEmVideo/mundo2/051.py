# Progressão aritmética
primeiro = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a razão: '))
print(f'Os 10 Primeiros Termos da PA com Razão {razao} e iniciada em {primeiro}):')
print(primeiro, end=' ')
for i in range(1, 10):
    primeiro += razao
    print(primeiro, end=' ')
print()
