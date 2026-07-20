'''
Class to manage sound effects for food consumption and game over.
Handles the initialization of sounds and playing them when needed.
'''
import os
import pygame
class Sound:
    def __init__(self):
        pygame.mixer.init()
        sound_path = 'sounds/'
        food_sound_path = os.path.join(sound_path, 'eat_food.wav')
        gameover_sound_path = os.path.join(sound_path, 'game_over.wav')
        if not os.path.exists(food_sound_path) or not os.path.exists(gameover_sound_path):
            raise FileNotFoundError(f"Sound files missing in {sound_path}")
        self.food_sound = pygame.mixer.Sound(food_sound_path)
        self.gameover_sound = pygame.mixer.Sound(gameover_sound_path)
    def play_food_consumption_sound(self):
        self.food_sound.play()
    def play_game_over_sound(self):
        self.gameover_sound.play()