import funções

funções.cabecalho('Desafio 107', 'MoedaRRrr')


p = float(input('Dígite o preço: R$'))
print(f'''A metade de R${p} é R${funções.metade(p)}
O dobro de R${p} é R${funções.metade(p)}
Aumentando 10%, temos R${funções.aumentar(p, 10)}
Reduzindo 13%, temos R${funções.diminuir(p, 13)}''')

