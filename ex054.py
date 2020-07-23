from datetime import date
from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 54', 'MAIORRrrRIDADERRrr')

maior = menor = 0

for c in range(7):
    nasc = int(input(f'Em que ano a {c+1}º pessoa nasceu? '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f'''Ao todo são {maior} maiores de idade
E {menor} menores de idade''')