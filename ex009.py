from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 9', 'PRESSÃO NENEM')

valor = int(input('Dígite um número para ver sua tabuada: '))
print('-'*25)
for vezes in range(1, 11):
    print(f'{valor} x {vezes} = {vezes*valor}')
print('-'*25)