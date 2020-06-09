import pygame
print(f'\033[40;31;1m{"Desafio 20":=^20}\033[m\n{"Julgamentor":^20}')

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
