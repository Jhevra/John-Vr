print(f'\033[40;33;1m{"Desafio 82":=^100}\033[m\n\033[40;31;1m{"DEPRESSÃO":^100}\033[m')
lista = list()
listapar = list()
listaimp = list()

while True:
    lista.append(int(input('Dígite um valor: ')))

    res = input('Quer continuar [S/N]? ').strip().upper()
    while res[0] != 'S' and res[0] != 'N':
        res = input('Quer continuar [S/N]? ').strip().upper()
    if res[0] == 'N':
        break

for valor in lista:
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimp.append(valor)
print(f'''A lista completa de valores é {sorted(lista)}
A lista de valores pares é {sorted(listapar)}
A lista de valores ímpares é {sorted(listaimp)}''')