from datetime import datetime

print(f'''\033[40;31;1m{"Desafio 92":=^20}\033[m\n\033[33;1m{"APOSENTARRr":^20}\033[m''')
pessoa = dict()
pessoa['Nome'] = input('Nome: ')
pessoa['Nascimento'] = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.today().year - pessoa['Nascimento']
pessoa['Ctps'] = int(input('Carteira de trabalho [0 = Não possue]: '))

if pessoa['Ctps'] == 0:
    print('-=' * 35)
    for k, v in pessoa.items():
        print(f' - {k} tem o valor {v}')

else:
    pessoa['Contratação'] = int(input('Anos de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] + 35) - pessoa['Nascimento']
    for k, v in pessoa.items():
        print(f' - {k} tem o valor {v}')