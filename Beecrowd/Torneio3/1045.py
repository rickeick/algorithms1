A, B, C = map(float, input().split())
if B > A: A, B = B, A
if C > A: A, C = C, A
if C > B: C, B = B, C
triangulo = not (A >= B + C or B >= A + C or C >= A + B)
if A**2 == B**2 + C**2 and triangulo:
    print('TRIANGULO RETANGULO')
if A**2 > B**2 + C**2 and triangulo:
    print('TRIANGULO OBTUSANGULO')
if A**2 < B**2 + C**2 and triangulo:
    print('TRIANGULO ACUTANGULO')
if A == B and A == C and triangulo:
    print('TRIANGULO EQUILATERO')
if (A == B and C != A and C != B) or (C == B and C != A) or (A == C and A != B) and triangulo:
    print('TRIANGULO ISOSCELES')
if not triangulo:
    print('NAO FORMA TRIANGULO')
