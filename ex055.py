from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 55', 'MENORRrr e MAIORRrr')

maior = menor = 0

for pessoa in range(5):
    p = float(input(f'Peso da {pessoa+1}º: '))
    if pessoa == 0:
        maior = menor = p
    else:
        if p > maior:
            maior = p

        if p < menor:
            menor = p

print('-'*45)
print(f'''O maior peso foi: {maior}Kg
E o menor peso foi: {menor}Kg''')