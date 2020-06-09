print(f'''\033[40;31;1m{"Desafio 34":=^20}\033[m\n\033[33;1m{"Ajustador":^20}\033[m''')
salario = float(input('Digite seu salário: '))
if salario > 1250:
    print(f'Seu aumento foi de R${(salario*10)/100:.2f}, Seu salário ficara R${(salario*10)/100+salario:.2f}')
else:
    print(f'Seu aumento foi de R${(salario*15)/100:.2f}, Seu salário ficara R${(salario*15)/100+salario:.2f}')
