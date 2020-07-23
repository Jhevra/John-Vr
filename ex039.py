from funções.UtilidadesCev.Dados import cabecalho
from datetime import datetime

cabecalho('Desafio 39', 'ALISTARRrr')

ano = int(input('Ano de nascimento: '))
idade = datetime.today().year - ano

if idade > 18:
    print('-'*45)
    print(f'''Quem nasceu em {ano} tem {idade} anos em {datetime.today().year}.
Você ja deveria ter se alistado há {idade - 18} anos. 
\033[31mSeu alistamento foi em {datetime.today().year - (idade - 18)}.\033[m''')

elif idade == 18:
    print('-'*45)
    print(f'''Quem nasceu em {ano} tem {idade} anos em {datetime.today().year}.
\033[33mVocê tem que se alistar IMEDIATAMENTE!\033[m''')

else:
    print('-' * 45)
    print(f'''Quem nasceu em {ano} tem {idade} anos em {datetime.today().year}.
\033[34mSeu alistamento sera daqui há {18 - idade} anos em {datetime.today().year + (18 - idade)}.\033[m''')

