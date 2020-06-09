

print(f'\033[40;33;1m{"Desafio 79":=^20}\033[m\n\033[40;31;1m{"BREAKDOWN":^20}\033[m')
numeros = list()
while True:
    n = int(input('Dígite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('\033[32;1mAdicionado com sucesso...\033[m')
    else:
        print('\033[31;1mValores duplicados serão ignorados...\033[m')
    res = input('Quer continuar? [S/N]: ').strip().upper()
    while res[0] != 'N' and res[0] != 'S':
        res = input('\033[31;1mERRO!\033[m Quer continuar? [S/N]: ').strip().upper()
    if res[0] == 'N':
        break

print('-='*35)
sorted(numeros)
print('Lista de valores dígitados: ')
for valor in numeros:
    print(valor, end='... ')
print()

