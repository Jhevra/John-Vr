import random
from math import tan, sin, radians, cos
print(f'{"Desafio 19":=^20}\n\033[40;31;1m{"Angulador":^20}\033[m')
angulo = random.uniform(-100.5, 100.5)
print(f'O angulo selecionado foi: \033[35;1m{angulo}\033[m')
print(f'''A tangente do angulo \033[33;1m{angulo:.3f}º\033[m é de \033[32;1m{tan(radians(angulo)):.3f}\033[m
O coseno do angulo \033[33;1m{angulo:.3f}º\033[m é de \033[32;1m{cos(radians(angulo)):.3f}\033[m 
O seno do angulo \033[33;1m{angulo:.3f}º\033[m é de \033[32;1m{sin(radians(angulo)):.3f}\033[m''')
