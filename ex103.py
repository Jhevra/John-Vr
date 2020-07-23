from funções.UtilidadesCev.Dados import cabecalho
from funções.UtilidadesCev.Functions import ficha

cabecalho('Desafio 103', 'FUTEBORRr')

print('-=' * 36)
jogador = input('Nome do Jogador: ')
gols = input('Números de gols: ')

while not gols.isnumeric():
    gols = input('\033[31;1mERRO!\033[m Números de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador.strip() == '':
    ficha(gols=gols)
else:
    ficha(jogador, gols)