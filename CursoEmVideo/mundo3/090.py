# Dicionários em python
aluno = {}
aluno['Nome'] = input('Nome do Aluno: ')
aluno['Média'] = float(input('Média do Aluno: '))
if aluno['Média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['Média'] <= 5:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Recuperação'
print()
for chave, valor in aluno.items():
    print(f'{chave} tem o valor {valor}')
