import random, math
print(f'{"Desafio 17":=^20}\n\033[40;31;1m{"Catetor":^20}\033[m')
oposto = float(random.uniform(0.1, 100.001))
adjacente = float(random.uniform(0.1, 100.001))
print(f'''Valor do oposto: \033[33;1m{oposto:.3f}\033[m
Valor do adjacente \033[33;1m{adjacente:.3f}\033[m''')
print(f'O valor da Hipotenusa concide em \033[32;1m{math.hypot(oposto, adjacente):.3f}\033[m')
