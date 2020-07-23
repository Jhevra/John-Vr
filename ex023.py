from random import randrange
from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 23', 'AAAAAAAAAAAAAAAAAARRRRRRRRRRRr')

num = int(randrange(1, 9999))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'''Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {u}''')

