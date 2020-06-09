import random

# Modo com STR
# print(f'\033[40;31;1m{"Desafio 22":=^20}\033[m\n\033[33;1m{"Unidader":^20}\033[m')
# num = int(random.randrange(1, 9999))
# n = str(num)
# print(f''' O numero escolhido foi {num}
# Unidade: {n[3]}
# Dezena: {n[2]}
# Centena: {n[1]}
# Milhar: {n[0]}
# ''')

# Modo Matematico
print(f'\033[40;31;1m{"Desafio 22":=^20}\033[m\n\033[33;1m{"Unidader":^20}\033[m')
num = int(random.randrange(0, 9999))
print(f''' O numero escolhido foi {num}
Unidade: {[num // 1 % 10]}
Dezena: {[num // 10 % 10]}
Centena: {[num // 100 % 10]}
Milhar: {[num // 1000 % 10]}''')

