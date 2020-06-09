print(f'''\033[40;33;1m{"Desafio 14":=^20}\033[m\n{"Conversor de Temperaturas"}''')
celsius = float(input('Digite o valor em ºC, que sera convertido em ºF: '))
print(f'''\033[0;32;1m{celsius}\033[mºC é exatamente \033[0;31;1m{(celsius*9/5)+32}\033[mºF''')
