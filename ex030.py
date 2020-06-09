print(f'''\033[40;31;1m{"Desafio 30":=^20}\033[m\n\033[33;1m{"IM ou PA":^20}\033[m''')
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número \033[34;1m{numero}\033[m é \033[32;1mPAR\033[m, {numero}/2 = {numero / 2:.0f}')
else:
    print(f'O número \033[34;1m{numero}\033[m é \033[31;1mIMPAR\033[m, {numero}/2 = {numero / 2:.1f}')
