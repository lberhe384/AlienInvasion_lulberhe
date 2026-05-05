"""Bullet module for Alien Invasion side-scrolling game."""

import pygame
from pathlib import Path


class Bullet:
    """A class to manage bullets fired from the ship."""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Load bullet image
        BASE_DIR = Path(__file__).parent
        self.image = pygame.image.load(BASE_DIR / "images" / "laser.png")

        self.rect = self.image.get_rect()

        # Start bullet at ship position (left side ship)
        self.rect.midleft = game.ship.rect.midright

        # Store position as float for smooth movement
        self.x = float(self.rect.x)

        # Speed (moves right)
        self.speed = 7

    def update(self):
        """Move the bullet horizontally to the right."""
        self.x += self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        self.screen.blit(self.image, self.rect)