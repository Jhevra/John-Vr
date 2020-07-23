from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 50', 'SOMARRrr PARRrr')
soma = 0

for c in range(6):
    valor = int(input(f'{c+1}º valor: '))
    if valor % 2 == 0:
        soma += valor
print('-'*45)
print(f'A soma dos valores pares foi \033[35m{soma}\033[m')