from random import randint
from time import sleep
print(f'\033[40;33;1m{"Desafio 88":=^20}\033[m\n\033[40;31;1m{"VIRADARR":^20}\033[m')
jogos = int(input('Quantos jogos serão feitos? : '))
print('-='*35)
print(f'{"Sorteando"} {jogos} Jogos')
print('-='*35)
for cont in range(0, jogos):
    megasena = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f'{cont+1}º JOGO >>> {sorted(megasena)}')
    sleep(1.5)
print(f'{"BOA SORTE":^20}')

