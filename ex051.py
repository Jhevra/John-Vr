from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 51', 'P.A RRrr')

print('-'*45)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(1, 11):
    print(primeiro, end=' ==> ')
    primeiro += razao
print('Acabou!')