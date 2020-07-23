from math import radians, cos, sin, tan
from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 18', 'COSENORRrr')

angulo = float(input('Dígite o ângulo: '))

print(f'''O ângulo de {angulo} tem o SENO de {sin(radians(angulo)):.2f}
O ângulo de {angulo} tem o COSSENO de {cos(radians(angulo)):.2f}
O ângulo de {angulo} tem TANGENTE de {tan(radians(angulo)):.2f}''')