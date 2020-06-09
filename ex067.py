print(f'\033[40;33;1m{"Desafio 67":=^20}\033[m\n\033[40;31;1m{"TABUDAOR":^20}\033[m')
cont = 1
while True:
    print('-'*20)
    tabs = int(input('Dígite um valor: '))
    print('-'*20)
    if tabs < 0:
        break
    for cont in range(1, 11):
        print(f'{tabs} X {cont} = {tabs*cont}')
    cont += 1
print('\033[31;1mERRO! NÚMERO NEGATIVO DETECTADO\033[m')