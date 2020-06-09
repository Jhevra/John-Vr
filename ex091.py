from random import randint
from time import sleep
from operator import itemgetter
print(f'''\033[40;31;1m{"Desafio 91":=^20}\033[m\n\033[33;1m{"RODARRr":^20}\033[m''')
jogadores = dict()
raking = dict()

for numeros in range(0, 4):
    jogadores[f'Jogador {numeros + 1}'] = randint(1, 6)

print(f'------------{"OS VALORES SORTEADOS FORAM"}------------')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()

print(f'------------{"RESULTADOS"}------------')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]} pontos')
    sleep(1)





