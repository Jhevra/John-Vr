from random import randint
print(f'\033[40;33;1m{"Desafio 74":=^20}\033[m\n\033[40;31;1m{"BREAKDOWN":^20}\033[m')

maior = menor = 0

lista = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print('Os números sorteados foram', end=' ')
for v in lista:
    print(v, end=' ')
print()
print(f'''O menor número é {min(lista)}
O maior número é {max(lista)}''')



