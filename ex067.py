from funções.UtilidadesCev.Dados import cabecalho

cabecalho('Desafio 67', 'TabuadaRRrr')


while True:
    n = 1

    print('-'*40)
    valor = int(input('Número: '))
    print('-' * 40)
    if valor < 0:
        print(f'\033[31mERRO! NÚMERO NEGATIVO DÍGITADO!\033[m')
        break

    while n != 11:
        print(f'{valor} x {n:<2} = {valor*n:<1}')
        n += 1