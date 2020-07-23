import funções

funções.cabecalho('Desafio 107', 'MoedaRRrr')


p = float(input('Dígite o preço: R$'))
print(f'''A metade de {funções.moeda(p)} é {funções.moeda(funções.metade(p))}
O dobro de {funções.moeda(p)} é {funções.moeda(funções.metade(p))}
Aumentando 10%, temos {funções.moeda(funções.aumentar(p, 10))}
Reduzindo 13%, temos {funções.moeda(funções.diminuir(p, 13))}''')
