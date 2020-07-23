print(f'\033[40;33;1m{"Desafio 85":=^100}\033[m\n\033[40;31;1m{"LISTARARAR":^100}\033[m')
lista = [[], []]
for cont in range(7):
    num = int(input(f'{cont+1}º Number: '))
    if num % 2 == 0:
        lista[0].append(num)
    if num % 2 == 1:
        lista[1].append(num)
print(f'''List of even numbers: {sorted(lista[0])}
List of odd numbers: {sorted(lista[1])}''')