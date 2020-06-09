print('{:=^20}\n'.format('Desafio 12'), 'Calculador de Desconto (%5)')
precototal = float(input('Digite o valor do produto: '))
desconto = float((precototal*5)/100)
print('usando o cupom ´AAHHH´ o produto que era R${:.2f},ficando assim R${:.2f}, ou seja, você ganhou R${:.2f} de desconto.'.format(precototal, precototal-desconto, desconto))
