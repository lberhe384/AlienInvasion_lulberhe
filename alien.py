from pygame.sprite import Sprite
import pygame
class Alien(Sprite):

    def __init__(self, game, x, y):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
    
        self.rect.x = x
        self.rect.y = y
        
    
    def update(self):
        self.rect.x += self.settings.alien_speed
        
            
            