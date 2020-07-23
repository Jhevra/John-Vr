print(f'''\033[40;31;1m{"Desafio 90":=^20}\033[m\n\033[33;1m{"MEDIARRR":^20}\033[m''')
ficha = dict()
ficha['Nome'] = input('Nome: ')
ficha['Média'] = float(input(f'Média de {ficha["Nome"]}: '))

print('-='*35)

if ficha['Média'] > 6:
    ficha['Situação'] = 'Aprovado'
else:
    ficha['Situação'] = 'Reprovado'

for k, v in ficha.items():
    print(f'    ==> {k} tem valor {v}')