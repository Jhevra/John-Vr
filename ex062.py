from funções.UtilidadesCev.Dados import cabecalho

cabecalho('Desafio 62', 'PaRRrr')

contador = 0

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

while contador != 10:
    print(primeiro, end=' -> ')
    primeiro += razao
    contador += 1
print('Acabou')
