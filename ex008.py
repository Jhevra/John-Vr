print(f'\033[40;33;1m{"Desafio 08":=^20}\033[m\n\033[40;33;1m{"Conversor de Medidas"}\033[m')
metros = float(input('Digite o valor em Metros (M): >> '))
print(f'''\033[1;31m{metros}\033[m metros é igual a \033[1;33m{metros*100}\033[m cm
\033[1;31m{metros}\033[m metros é igual a \033[1;33m{metros*1000}\033[m mm
''')
