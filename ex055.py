print(f'\033[40;33;1m{"Desafio 55":=^20}\033[m\n\033[40;31;1m{"PESOR":^20}\033[m')
lista = list()
for pessoa in range(1, 6):
    lista.append(float(input(f'Dígite o peso da {pessoa}º pessoa: ')))
print(f'''O menor peso entre as pessoas foi de {min(lista)}Kg 
E o maior foi de {max(lista)}Kg''')