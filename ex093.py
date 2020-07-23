print(f'''\033[40;31;1m{"Desafio 93":=^20}\033[m\n\033[33;1m{"CADASTRARRr":^20}\033[m''')

jogador = dict()
estaticas = list()

#######################################################################################################################
jogador['Nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(partidas):
    estaticas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['Gols'] = estaticas
jogador['Total'] = sum(estaticas)
#######################################################################################################################
print('-='*40)
print(jogador)
print('-='*40)
#######################################################################################################################
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
#######################################################################################################################
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])}')
for i, v in enumerate(jogador['Gols']):
    print(f'    ==> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')