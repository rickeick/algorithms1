# Aumentos multiplos
total = 0
aumento = 0
salario = float(input('Qual o salário do funcionário? R$'))
if salario > 1250:
    aumento = (salario * 10) / 100
    total = salario + aumento
else:
    aumento = (salario * 15) / 100
    total = salario + aumento
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${total:.2f} agora')
