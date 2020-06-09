print(f'''\033[40;31;1m{"Desafio 93":=^20}\033[m\n\033[33;1m{"CADASTRARRr":^20}\033[m''')

jogador = dict()
partida = list()

#######################################################################################################################
jogador['Nome'] = input('Nome do jogador: ')
jogos = (int(input(f'Quantas partidas {jogador["Nome"]} jogou? ')))
for c in range(jogos):
    partida.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
#######################################################################################################################
print('-='*35)
print(jogador)
#######################################################################################################################
print('-='*35)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
#######################################################################################################################
print('-='*35)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'==> Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]}')