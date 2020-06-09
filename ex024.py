print(f'''\033[40;31;1m{"Desafio 24":=^20}\033[m\n\033[33;1m{"Santor":^20}\033[m''')
cidade = input('Digite o nome de sua cidade: ').strip()
cidade = cidade.upper().split()
print(f'''Sua cidade começa com santo: \033[35;1m{'SANTO' in cidade[0]}\033[m
\033[32;1m[True = Verdade]\033[m\n\033[31;1m[False = Falso]\033[m''')
