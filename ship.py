import pygame
from pathlib import Path
    #Ai usage diclosure for editing 
class Ship:
     """Represents the player's ship moving vertically on the left side."""


     def __init__(self, game):
        """Initialize ship at the left edge of the screen."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        BASE_DIR = Path(__file__).parent
        self.image = pygame.image.load(BASE_DIR / "images" / "ship.png")


        self.rect = self.image.get_rect()
      
        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)
        self.speed = 3
        self.moving_up = False
        self.moving_down = False
    

#I drafted this announcement myself, then used ChatGPT to help polish the tone,

     def update(self):
        """Update ship movement."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        self.rect.y = self.y
     def blitme(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)
    
        


        