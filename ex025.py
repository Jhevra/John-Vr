print(f'''\033[40;31;1m{"Desafio 25":=^20}\033[m\n\033[33;1m{"Silvador":^20}\033[m''')
nome = input('Digite seu nome completo: ').strip().lower()
print(f'''No seu nome tem Silva? \033[36;1m{'Silva' in nome.lower()}\033[m
\033[32;1m[True = Verdade]\033[m\n\033[31;1m[False = Falso]\033[m
''')
