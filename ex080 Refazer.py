print(f'\033[40;33;1m{"Desafio 80":=^100}\033[m\n\033[40;31;1m{"BREAKDOWN":^100}\033[m')
lista = list()

for cont in range(5):
    n = int(input('Dígite um valor: '))
    if cont == 1 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos <= len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print(lista)



