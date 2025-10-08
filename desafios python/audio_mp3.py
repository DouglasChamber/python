import os
import pygame

# Garante que o diretório de trabalho seja o mesmo do script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()

input("Pressione Enter para parar a música...")
pygame.mixer.music.stop()
