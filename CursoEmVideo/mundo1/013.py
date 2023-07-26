# Reajuste salarial
salario = float(input('Qual é o salário do funcionário R$'))
reajuste = (salario * 15) / 100
total = salario + reajuste
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${total:.2f}')
