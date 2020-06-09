print(f'\033[40;31;1m{"Desafio":=^20}\033[m\n\033[33;1m{"Nomer":^20}\033[m')
nomec = str(input('Digite seu nome: ')).strip().split()
print(f'''Seu primeiro nome é {nomec[0]}
Seu ultimo nome é {nomec[len(nomec)-1]}
''')
