
print(f'\033[40;33;1m{"Desafio 81":=^100}\033[m\n\033[40;31;1m{"DEPRESSÃO":^100}\033[m')
lista = list()


while True:
    lista.append(int(input('Dígite um valor: ')))

    res = input('Quer continuar [S/N]? ').strip().upper()
    while res[0] != 'S' and res[0] != 'N':
        res = input('Quer continuar [S/N]? ').strip().upper()
    if res[0] == 'N':
        break

print('-='*35)
print(f'''Foram dígitados {len(lista)} valores
A lista de valores em ordem decrescente: {sorted(lista, reverse=True)}''')

if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não faz parte da lista')
