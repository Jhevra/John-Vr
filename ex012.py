from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 12', 'DescontoRRrr')

valor = float(input('Qual é o preço do produto? R$'))

desconto = (valor*5)/100

print(f'O produto que custava R${valor:.2f}, na promoção com desconto de 5% vai custa R${valor-desconto:.2f}')
