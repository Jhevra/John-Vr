print(f'''\033[40;33;1m{"Desafio 15":=^20}\033[m
\033[0;33;1m{"Aluguel de Carros":^20}\033[m''')
dias = float(input(f'Por quantos \033[0;31;1mdias\033[m o carro foi alugado: '))
km = float(input(f'Quantos \033[0;31;1mKM\033[m foram rodados com o carro: '))
print(f'O valor total a ser pago é de \033[0;32;1mR${(60*dias)+(0.15*km):.2f}\033[m')
