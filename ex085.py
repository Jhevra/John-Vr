print(f'\033[40;33;1m{"Desafio 85":=^20}\033[m\n\033[40;31;1m{"LISTARARAR":^20}\033[m')
lista = [[], []]
for c in range(0, 7):
    numeros = int(input('Dígite um valor: '))
    if numeros % 2 == 0:
        lista[0].append(numeros)
    else:
        lista[1].append(numeros)
print('-='*55)
print(f'''Os valores pares dígitados foram: \033[32;1m{sorted(lista[0])}\033[m
Os valores ímpares dígitados foram: \033[31;1m{sorted(lista[1])}\033[m''')
