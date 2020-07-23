import funções

funções.cabecalho('Desafio 107', 'MoedaRRrr')


p = float(input('Dígite o preço: R$'))
formatar = int(input('Quer o resultado formatado? [1 - Sim | 2 - Não]: '))

if formatar == 1:
    formatar = True

elif formatar == 2:
    formatar = False

else:
    while formatar != 1 and formatar != 2:
        formatar = int(input('\033[31;1mERRO!\033[mQuer o resultado formatado? [1 - Sim | 2 - Não]: '))

print(f'''A metade de {funções.moeda(p)} é {funções.metade(p, formatar)}
O dobro de {funções.moeda(p)} é {funções.dobro(p, formatar)}
Aumentando 10%, temos {funções.aumentar(p, 10, formatar)}
Reduzindo 13%, temos {funções.diminuir(p, 13, formatar)}''')
