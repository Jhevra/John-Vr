print(f'\033[40;33;1m{"Desafio 86":=^20}\033[m\n\033[40;31;1m{"MATRIZZ":^20}\033[m')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Número para [{l}, {c}]: '))
print('-='*35)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
