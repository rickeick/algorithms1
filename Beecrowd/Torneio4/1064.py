n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
positivos = list()
total = int()
if n1 > 0: positivos.append(n1)
if n2 > 0: positivos.append(n2)
if n3 > 0: positivos.append(n3)
if n4 > 0: positivos.append(n4)
if n5 > 0: positivos.append(n5)
if n6 > 0: positivos.append(n6)
print(f'{len(positivos)} valores positivos')
for n in positivos: total += n
media = total / len(positivos)
print(f'{media:.1f}')
