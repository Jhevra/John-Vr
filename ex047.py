print(f'''\033[40;31;1m{"Desafio 47":=^20}\033[m\n\033[33;1m{"PARR":^20}\033[m''')

# for cont in range(0, 51, 2):
#     print(cont, end=' ==>')

for cont in range(0, 51):
    if cont % 2 == 0:
        print(cont, end=' ==> ')
print('Acabou')