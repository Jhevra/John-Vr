from random import randint
from time import sleep
from operator import itemgetter
print(f'''\033[40;31;1m{"Desafio 91":=^100}\033[m\n\033[33;1m{"RODARRr":^100}\033[m''')
jogadores = dict()
raking = list()

# Randomizing player values
for cont in range(4):
    jogadores[f'{cont+1}º Jogador'] = randint(1, 6)

print('-='*35)
print(f'{"Valores Sorteados":^70}')
print('-='*35)

# Showing player point
for k, v in jogadores.items():
    print(f'    ==> O {k} tirou {v}')
print('-='*35)
# Showing the results
raking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(raking):
    print(f'{i+1}º lugar: {v[0]} tirou {v[1]} no dado')
    sleep(1)

