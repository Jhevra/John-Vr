print(f'\033[40;33;1m{"Desafio 60":=^20}\033[m\n\033[40;31;1m{"FATORIALR":^20}\033[m')
num = int(input('Dígite um valor para ser feito o fatorial: '))
c = num
for cont in range(2, num+1):
    print('\033[32;1m',c, '\033[m')
    c = cont*c



