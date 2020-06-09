
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
print(f'''Você dígitou {len(lista)} elementos
Os valores dígitados em ordem decresente: {sorted(lista, reverse=True)}''')

if 5 in lista:
    print(f'\033[32;1mO número 5 faz parte da lista\033[m')
else:
    print(f'\033[31;1mO número 5 não faz parte da lista\033[m')