# Aprovando empréstimo
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos deseja pagar: '))
prestacao = casa / (anos * 12)
minimo = (salario * 30) / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos')
print(f'A prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print("Empréstimo CONCEDIDO!")
else:
    print('Empréstimo NEGADO!')
