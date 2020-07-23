from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 60', 'FatoriaRRrr')

valor = int(input('Dígite valor: '))

c = valor
fat = 1

while valor != 1:
    fat *= valor
    valor -= 1
    print(fat)


