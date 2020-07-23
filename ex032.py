from datetime import date
from funções.UtilidadesCev.Dados import cabecalho

cabecalho('Desafio 32', 'ANORRrr')

ano = int(input('Qual ano será analisado (coloque 0 para ser analisado o ano atual) : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
