print(f'\033[40;33;1m{"Desafio 78":=^20}\033[m\n\033[40;31;1m{"M&M LIST":^20}\033[m')

# def verificar(extremos):
#     for pos, valor in enumerate(lista):
#         if valor == extremos:
#             print(f'\033[33;1m{pos+1}...\033[m', end=' ')
#     print()


lista = list()

for cont in range(5):
    lista.append(int(input(f'Valor para a {cont + 1}º posição: ')))

print('-=' * 36)
print(f'''Você dígitou os valores {sorted(lista)}
O maior valor dígitado foi {max(lista)} nas posições''', end=' ')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i+1}...', end=' ')
print()
print(f'''O menor valor dígitado foi {min(lista)} nas posições''', end=' ')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i+1}...', end=' ')
