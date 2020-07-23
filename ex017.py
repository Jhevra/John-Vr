from math import hypot
from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 17', 'HIPOTENUSA DO MEU PAU')

oposto = (input('Comprimento do cateto oposto: ')).replace(',', '.')
oposto = float(oposto)
adjascente = (input('Comprimento do cateto adjacente: ')).replace(',', '.')
adjascente = float(adjascente)

print('-'*45)

print(f'A hipotenusa vai medir \033[33m{hypot(oposto, adjascente):.3f}\033[m')
