A, B, C, D = map(float, input().split())
media = (A*2 + B*3 + C*4 + D*1) / 10
print(f"Media: {media:.1f}")
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    nova = (media + exame) / 2
    if nova >= 5.0: print("Aluno aprovado.")
    else: print("Aluno reprovado.")
    print(f"Media final: {nova:.1f}")
