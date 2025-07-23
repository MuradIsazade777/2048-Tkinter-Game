import os
import pygame
pygame.init()
pygame.mixer.init()
sounds_dir = os.path.join(os.path.dirname(__file__), '..', 'sounds')
sounds_dir = os.path.abspath(sounds_dir)

def play_merge():
    pygame.mixer.Sound(os.path.join(sounds_dir, "merge.wav")).play()

def play_move():
    pygame.mixer.Sound(os.path.join(sounds_dir, "move.wav")).play()

def play_win():
    pygame.mixer.Sound(os.path.join(sounds_dir, "game_win.wav")).play()

def play_game_over():
    pygame.mixer.Sound(os.path.join(sounds_dir, "game_over.wav")).play()