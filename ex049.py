print(f'''\033[40;31;1m{"Desafio 49":=^20}\033[m\n\033[33;1m{"TABUDAOR 2.0":^20}\033[m''')
inicio = int(input('Dígite um valor: '))
for cont in range(1, 11):
    print(f'{inicio} x {cont} = {inicio*cont}')
    cont += 1