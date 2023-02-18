# Aquele clássico de média
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print(f'O aluno tem média igual a {media:.1f}')
if media > 6:
    print('APROVADO')
else:
    print('REPROVADO')
