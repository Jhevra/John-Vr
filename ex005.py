print(f'\033[40;35;1m{"Desafio 05":=^25}\033[m')
valor = int(input('Digite um numero e mostrarei seu sucessor e antecessor: >> '))
print(f'''O antecessor de\033[1;34;1m {valor}\033[m é \033[1;31;1m{valor-1}\033[m.
O sucessor de \033[1;34;1m{valor}\033[m é \033[1;32;1m{valor+1}\033[m.
\033[40;33;1m{"Fim do Desafio":=^20}\033[m
''')
