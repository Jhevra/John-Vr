from funções.UtilidadesCev.Dados import cabecalho
from math import trunc


cabecalho('Desafio 16', 'Quebrando TOTALMENTE ISAAC NEWTON')

valor = float(input('Dígite um valor: '))
print(f'O valor dígitado foi {valor} e sua porção inteira é {int(valor)}')

print(f'O valor digitado foi {valor} e sua porção inteira {trunc(valor)}')