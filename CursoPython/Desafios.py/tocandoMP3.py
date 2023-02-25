#tocando um mp3

import pygame  # Importa o módulo Pygame

pygame.init()  # Inicia o módulo Pygame

# Carrega o arquivo de música "favelavive5.mp3"
pygame.mixer.music.load('/home/lazaro/Área de Trabalho/Estudando_Python/CursoPython/Desafios.py/favelavive5.mp3')

# Inicia a reprodução da música
pygame.mixer.music.play()

# Loop que espera a música terminar de tocar
while pygame.mixer.music.get_busy():
    # Limita o framerate para 30 quadros por segundo
    pygame.time.Clock().tick(30)

# Finaliza o módulo Pygame
pygame.quit()
