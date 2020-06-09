print(f'\033[40;33;1m{"Desafio 66":=^20}\033[m\n\033[40;31;1m{"BREAKDOWN":^20}\033[m')
print('''===========================================
=               BANCO THOSEN              =
===========================================''')
valor = int(input('Dígite o valor a ser sacado: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de {ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

