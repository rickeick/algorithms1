# Validação de dados
sexo = str(input('informe seu sexo [M/F]: '))
while sexo not in ['M', 'F', 'm', 'f']:
    sexo = str(input('Dados inválidos. por favor informe seu sexo [M/F]: '))
print('Sexo {sexo} registrado com sucesso')
