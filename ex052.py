from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 52', 'PRIMORRrr')

div = 0
valor = int(input('Valor: '))
for c in range(1, valor+1):
    if valor % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        div += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print()
print('-'*45)
if div == 2:
    print(f'''O número {valor} foi divisível {div} vezes
E por isso ele é primo''')
else:
    print(f'''O número {valor} foi divisível {div} vezes
E por isso ele não é primo''')