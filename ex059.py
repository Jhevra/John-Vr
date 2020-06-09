from time import sleep
print(f'''\033[40;31;1m{"Desafio 59":=^20}\033[m\n\033[33;1m{"MENUR":^20}\033[m''')
lista = list()

for cont in range(0, 2):
    lista.append(int(input('Dígite um valor: ')))

opcao = 0

while opcao != 5:
    opcao = int(input('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR
Escolha uma opção: '''))
    print('-'*20)

    if opcao == 1:
        print(lista[0] + lista[1], '\n')
        print('-'*20)

    elif opcao == 2:
        print(lista[0] * lista[1], '\n')
        print('-' * 20)

    elif opcao == 3:
        print(max(lista), '\n')
        print('-' * 20)

    elif opcao == 4:
        lista.remove(lista[0])
        lista.remove(lista[0])
        lista.append(int(input('Dígite um novo valor: ')))
        lista.append(int(input('Dígite um novo valor: ')))
        print('-' * 20)
