nome = str(input('Digite seu nome completo, para que seja analisado: '))
divido = nome.split()
print(f'''Seu nome em maiúsculo {nome.upper()}
Seu nome em minúsculo {nome.lower()}
A quantidades de letras no seu é de {len(nome.strip())}
O seu primeiro no tem {len(divido[0])} letras
''')
