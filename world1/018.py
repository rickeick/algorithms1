# Seno, cosseno e tangente
import math
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo}° tem seno de {seno:.3f}')
print(f'O ângulo de {angulo}° tem cosseno de {cosseno:.3f}')
print(f'O ângulo de {angulo}° tem tangente de {tangente:.3f}')
