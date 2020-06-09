print(f'\033[40;33;1m{"Desafio 51":=^20}\033[m\n\033[40;31;1m{"PAr":^20}\033[m')
print(f'''{"-=" * 20}
{"Progressão Aritimetrica":^40}
{"-=" * 20}''')
pt = int(input('Dígite o primeiro: '))
ulttermo = int(input('Até que termo você quer: '))
rz = int(input('Dígite a razão: '))
for cont in range(1, ulttermo+1):
    print(pt, end=' ==> ')
    pt += rz
print('Acabou!')
