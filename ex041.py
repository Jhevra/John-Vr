from datetime import date

print(f'''\033[40;31;1m{"Desafio 41":=^20}\033[m\n\033[33;1m{"Nadador":^20}\033[m''')
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
if idade <= 9:
    print('\033[35;1mAtleta Mirim\033[m')
elif idade <= 14:
    print('\033[34;1mAtleta Infantil\033[m')
elif idade <= 19:
    print('\033[33;1mAtleta Junior\033[m')
elif idade == 20:
    print('\033[32;1mAtleta Sênior\033[m')
else:
    print('\033[31;1mAtleta Master\033[m')
