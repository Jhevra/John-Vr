from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 70', 'MERCADORRrr')

cont = 0
total = maismil = barato = 0
baratoproduto = ''

while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))

    print('='*30)

    total += preco

    if cont == 0:
        barato = preco
        baratoproduto = produto
    else:
        if preco < barato:
            barato = preco
            baratoproduto = produto

    cont += 1

    if preco > 1000:
        maismil += 1

    resp = input('Quer continuar? [S/N] ').strip().upper()

    print('=' * 30)

    if resp == 'N':
        break

print(f'''--------- FIM DO PROGRAMA ---------
O total da compra foi R${total:.2f}
Temos {maismil} produtos custando mais de R$1000.00
O produto mais barato foi {baratoproduto} que custa R${barato:.2f}''')