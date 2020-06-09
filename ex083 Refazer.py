print(f'\033[40;33;1m{"Desafio 83":=^20}\033[m\n\033[40;31;1m{"EXPRESSADOR":^20}\033[m')
lista = list()

expr = input('Expressão Matematica: ')

for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Valida')
else:
    print('Invalida')