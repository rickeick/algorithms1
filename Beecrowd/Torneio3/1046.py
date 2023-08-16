inicio, fim = map(int, input().split())
if inicio == fim:
    print('O JOGO DUROU 24 HORA(S)')
elif inicio < fim:
    print(f'O JOGO DUROU {fim - inicio} HORA(S)')
elif inicio > fim:
    print(f'O JOGO DUROU {24 - (inicio - fim)} HORA(S)')
