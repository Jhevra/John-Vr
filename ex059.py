from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 59', 'CriaRRrr Menu')

lista = []

for c in range(2):
    lista.append(int(input(f'{c+1}º valor: ')))

opc = maior = 0

while opc != 5:
    print('-='*30)
    opc = int(input(f'''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
>>>>> Qual é a sua opcão? '''))
    print('-'*30)

    if opc == 1:
        somar = lista[0] + lista[1]
        print(f'{lista[0]} + {lista[1]} = {somar}')
        print('-' * 30)

    elif opc == 2:
        mult = lista[0] * lista[1]
        print(f'{lista[0]} * {lista[1]} = {mult}')
        print('-' * 30)

    elif opc == 3:
        print(f'O maior número foi {max(lista)}')
        print('-' * 30)

    elif opc == 4:
        lista.remove(lista[0])
        lista.remove(lista[0])
        for cont in range(2):
            lista.append(int(input(f'{cont+1}º valor: ')))
        print('-' * 30)

    else:
        print(f'\033[31;1m ===== FECHANDO.... =====\033[m')
        break