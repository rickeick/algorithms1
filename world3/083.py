# Validando expressões
pilha = []
expressao = input('Digite uma expressão: ')
for letra in expressao:
    if letra == '(':
        pilha.append('(')
    elif letra == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) > 0:
    print('Sua expressão está inválida')
else:
    print('Sua expressão está válida')
