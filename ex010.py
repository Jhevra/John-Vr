from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 10', 'DolaRRrr')

real = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${real} você pode comprar US${real*5.31:.2f}')