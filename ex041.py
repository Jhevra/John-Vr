from datetime import date
from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 41', 'NADARRrr')

nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento

print('-'*50)

if idade < 9:
    print(f'''O atleta tem {idade} anos.
CLASSIFICAÇÃO: MIRIM''')

elif 9 < idade < 14:
    print(f'''O atleta tem {idade} anos.
CLASSIFICAÇÃO: INFANTIL''')

elif 14 < idade < 19:
    print(f'''O atleta tem {idade} anos.
CLASSIFICAÇÃO: JÚNIOR''')

elif 19 < idade < 25:
    print(f'''O atleta tem {idade} anos.
CLASSIFICAÇÃO: SÊNIOR''')

else:
    print(f'''O atleta tem {idade} anos.
CLASSIFICAÇÃO: MASTER''')