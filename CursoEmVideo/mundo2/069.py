# Análise de dados do grupo
vinte = 0
dezoito = 0
masculino = 0
while True:
    idade = int(input('Qual sua  idade ?'))
    sexo = str(input('Digite seu sexo F/M')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('digite seu sexo F/M')).strip().upper()[0]
    opcao = str(input('deseja parar? digite N se não S ')).strip().upper()[0]
    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F':
        if idade >= 20:
            vinte += 1
    if opcao == 'N':
        break
print(f'Tem {dezoito} pessoas maior de 18')
print(f'Tem {masculino} pessoas do sexo masculino')
print(f'Tem {vinte} mulheres acima de 20 anos ')
