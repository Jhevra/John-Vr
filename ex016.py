import random, math
print(f'{"Desafio 16":=^20}\n{"Inteirador"}')
num = random.uniform(1.5, 100.5)
print(f'De \033[0;31;1m{num:.3f}\033[m para, \033[0;32;1m{math.trunc(num)}\033[m')
