from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 49', 'TabuadaRRrr')

valor = int(input('Valor: '))

print('-'*15)
for c in range(1, 11):
    print(f'{valor} x {c:>2} = {valor*c}')
print('-'*15)