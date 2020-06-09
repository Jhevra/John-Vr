print(f'''\033[40;31;1m{"Desafio 36":=^20}\033[m\n\033[33;1m{"Emprestimor":^20}\033[m''')
valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salario: R$'))
anos = int(input('Digite em quantos anos sera parcelado: '))
emprestimo = valor/(anos * 12) # O emprestimo será feito com o valor da casa sendo parcelado em meses
if emprestimo < (salario*30)/100: # Se o emprestimo for menor que 30% do salario
    print(f'Seu emprestimo será de R${emprestimo:.2f}')
else:
    print(f'Seu emprestimo execedeu o limite de 30% de seu salario, o emprestimo foi negado')