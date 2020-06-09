from datetime import date

print(f'''\033[40;31;1m{"Desafio 39":=^20}\033[m\n\033[33;1m{"Alistador":^20}\033[m''')
nascimento = int(input('Em que ano você nasceu? '))
idade = date.today().year - nascimento
if idade == 17:
    print('Está na hora de se alistar!')
elif idade < 17:
    print('Ainda não na hora jovem!')
    print(f'Falta {17 - idade} anos')
else:
    print('Ja passou da hora.')
    print(f'Faz {idade - 17}')
