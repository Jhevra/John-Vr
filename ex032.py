from datetime import date

print(f'''\033[40;31;1m{"Desafio 32":=^20}\033[m\n\033[33;1m{"Ano Bissexto":^20}\033[m''')
ano = int(input('Qual ano será analisado (coloque 0 para ser analisado o ano atual) : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
