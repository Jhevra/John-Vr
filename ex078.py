print(f'\033[40;33;1m{"Desafio 78":=^20}\033[m\n\033[40;31;1m{"M&M LIST":^20}\033[m')


def verificar(extremos):
    for pos, valor in enumerate(lista):
        if valor == extremos:
            print(f'\033[33;1m{pos+1}...\033[m', end=' ')
    print()


lista = list()

for cont in range(5):
    lista.append(int(input(f'Dígite um valor para posição {cont + 1}: ')))

print('-=' * 35)

print(f'Os números dígitados foram {lista}')

print(f'O maior valor dígitado foi \033[32;1m{max(lista)}\033[m na posição ', end=' ')
verificar(max(lista))

print(f'O menor valor dígitado foi \033[32;1m{min(lista)}\033[m na posição ', end=' ')
verificar(min(lista))

