print(f'''\033[40;31;1m{"Desafio 31":=^20}\033[m\n\033[33;1m{"Calculador":^20}\033[m''')
km = float(input('Digite a distancia da sua viagem em Km: '))
if km > 200:
    print(f'O custo total da viagem foi de \033[32;1mR${km*0.45:.2f}\033[m')
else:
    print(f'O custo total da sua viagem foi de \033[32;1mR${km*0.50:.2f}\033[m')
print(f'{"Fim":=^20}')
