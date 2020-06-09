print(f'''\033[40;31;1m{"Desafio 47":=^20}\033[m\n\033[33;1m{"IMPARR":^20}\033[m''')
soma = tot = 0
for cont in range(1, 500):
    if cont % 2 == 1:
        if cont % 3 == 0:
            soma += cont
            tot += 1
print(f'A soma dos {tot} valores solicitados foi de {soma}')