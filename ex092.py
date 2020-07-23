from datetime import datetime

print(f'''\033[40;31;1m{"Desafio 92":=^20}\033[m\n\033[33;1m{"APOSENTARRr":^20}\033[m''')
pessoa = dict()
pessoa['Nome'] = input('Nome: ')
anodenascimento = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.today().year - anodenascimento
pessoa['CTPS'] = int(input('Cateira de Trabalho [0 não tem]: '))

if pessoa['CTPS'] == 0:
    print('-='*35)
    for dado, entrada in pessoa.items():
        print(f'     ==> {dado} tem valor {entrada}')


else:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] + 35) - datetime.now().year
    print('-='*38)
    for k, v in pessoa.items():
        print(f'    - {k} tem valor {v}')
