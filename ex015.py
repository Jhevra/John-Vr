from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 15', 'VRUM VRUM...')

dias = int(input('Quantos dias alugas? '))
quilomestros = float(input('Quantos quilometros rodados? '))
total = (dias*60) + (quilomestros*0.15)
print(f'O total a pagar é de \033[32mR$\033[m\033[33;1m{total:.2f}\033[m')