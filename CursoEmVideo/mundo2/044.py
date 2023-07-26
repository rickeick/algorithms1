# Gerenciador de pagamento
produto = float(input('Qual é o preço normal do produto? R$ '))
print('Formas de Pagamento:')
print('[1] À vista em dinheiro/cheque (10% de desconto)')
print('[2] À vista no cartão de crédito (5% de desconto)')
print('[3] Parcelado em até 12x no cartão de crédito (20% de juros a partir de 3x)')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    valor = produto - (produto / 10)
    print('O produto à vista em dinheiro/cheque, com 10% de desconto')
    print(f'fica de R$ {produto:.2f} por R$ {valor:.2f}!')
elif opcao == 2:
    valor = produto - (produto / 20)
    print('O produto à vista no cartão de crédito, com 5% de desconto')
    print(f'fica de R$ {produto:.2f} por R$ {valor:.2f}!')
elif opcao == 3:
    parcelas = int(input('Em quantas vezes deseja parcelar? Digite um número de 2 a 12: '))
    if parcelas == 2:
        valor = produto / parcelas
        print(f'O produto em {parcelas}x no cartão de crédito')
        print(f'fica de R$ {produto:.2f} por {parcelas}x R$ {valor:.2f}!')
    else:
        juros = (produto / 5)
        valor = (produto + juros) / parcelas
        print(f'O produto em {parcelas}x no cartão de crédito')
        print(f'fica de R$ {produto:.2f} por {parcelas}x R$ {valor:.2f}!')
