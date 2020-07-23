from funções.UtilidadesCev.Dados import cabecalho
from math import sqrt
cabecalho('Desafio 6', 'Uno rebaixado')

valor = input('Dígite um número: ').replace(',', '.')
valor = float(valor)
print('-'*45)

print(f'''O dobro de {valor} é {valor*2}
O triplo de {valor} é {valor*3}
O raiz quadrada de {valor} é igual a {sqrt(valor):.2f}''')