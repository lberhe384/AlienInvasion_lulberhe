

import pygame
from pathlib import Path

"""Laser module: defines laser fired from the ship."""
class Laser(pygame.sprite.Sprite):
     """A laser fired from the ship that moves horizontally."""

     def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        BASE_DIR = Path(__file__).parent
        self.image = pygame.image.load(BASE_DIR / "images" / "laserBlast.png")

        self.rect = self.image.get_rect()

        # start at ship (right side of ship)
        self.rect.midleft = game.ship.rect.midright

        self.x = float(self.rect.x)
        self.speed = 8

     def update(self):
        """Move laser right."""
        self.x += self.speed
        self.rect.x = self.x

     def draw_laser(self):
        """Draw laser."""
        self.screen.blit(self.image, self.rect)
        
    #Used AI for intndetion 