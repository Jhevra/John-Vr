from random import randint
from time import sleep
print(f'\033[40;33;1m{"Desafio 88":=^20}\033[m\n\033[40;31;1m{"VIRADARR":^20}\033[m')
jogos = int(input('Quantos jogos serão feitos?: '))
print(f'-=-=-= FAZENDO {jogos} JOGOS -=-=-=')
for games in range(jogos):
    lista = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
    print(f'{games+1}º JOGO: {lista}')
    sleep(0.5)
print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'{" GOOD LUCK! ":-^30}')
print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

