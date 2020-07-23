print(f'''\033[40;31;1m{"Desafio 93":=^100}\033[m\n\033[33;1m{"CADASTRARRr":^100}\033[m''')

jogador = dict()
estaticas = list()
time = list()
while True:
    estaticas.clear()
    jogador.clear()
    jogador['Nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(partidas):
        estaticas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = estaticas[:]
    jogador['Total'] = sum(estaticas)
    time.append(jogador.copy())
    res = input('Quer continuar? [S/N]: ').strip().upper()
    while res[0] != 'N' and res[0] != 'S':
        res = input('Quer continuar? [S/N]: ').strip().upper()
    if res[0] == 'N':
        break

print('-='*36)
print('cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    opc = int(input('Mostrar dados de que jogador? (999 para parar): '))
    if opc >= len(time):
        print('\033[31;1mERRO!\033[m')
        opc = int(input('Mostrar dados de que jogador? (999 para parar): '))
    if opc == 999:
        break
    print(f'-- LEVANTAMENTE DO JOGADOR {time[opc]["Nome"]}: ')
    for i, v in enumerate(time[opc]['Gols']):
        print(f'    ==> Na partida {i+1}, fez {v} gols.')

    print('-'*40)