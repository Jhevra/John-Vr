print(f'\033[40;33;1m{"Desafio 86":=^20}\033[m\n\033[40;31;1m{"MATRIZZ":^20}\033[m')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Dígite um valor para [{linha}:{coluna}]'))
print('-='*35)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
