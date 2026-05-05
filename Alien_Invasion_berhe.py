"""
Program Name: Custom Game Mechanics
Author: Lewam Berhe
Purpose:Milestone 2  Implement Fleet and Collision Logic
Starter Code: Github
Date: May 2, 2026
"""
import sys
import pygame
from ship import Ship
from alien import Alien
from laser import Laser
from setting import Settings 
from button import Button
from game_stats import GameStats
from Scoreboard import Scoreboard

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
    
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.screen_rect = self.screen.get_rect()
        self.stats = GameStats()
        self.sb = Scoreboard(self)
        
        self.game_active = False

        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.laser= pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Play")
       

    def run_game(self):
        print("GAME LOOP ACTIVE")
        while True:
            self._check_events()

            if self.game_active:

                self.ship.update()
                self.laser.update()
                self._update_laser()

                self.aliens.update()

            
                self._check_collisions()
                self._check_loss()

            self._update_screen()



    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_laser()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                  mouse_pos = pygame.mouse.get_pos()
                  if self.play_button.rect.collidepoint(mouse_pos):
                     self.game_active = True
                     pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):

        if self.play_button.rect.collidepoint(mouse_pos):

            self.game_active = True
            pygame.mouse.set_visible(False)


            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_lives()

            self.laser.empty()
            self.aliens.empty()
            self._create_fleet()   

            self.ship.center_ship()
            self.settings.initialize_dynamic_settings()

    def _fire_laser(self):
        laser = Laser(self)
        self.laser.add(laser)

        
    def _update_laser(self):
        for laser in self.laser.copy():
            if laser.rect.left >= self.screen_rect.right:
                self.laser.remove(laser)

    def _check_collisions(self):
       collisions = pygame.sprite.groupcollide(
           self.laser, self.aliens, True, True
       )
       if collisions:
           self.stats.score += 10
           self.sb.prep_score()
           if self.stats.score > self.stats.high_score:
               self.stats.high_score = self.stats.score
               self.sb.prep_high_score()
   
    def _check_loss(self):
            for alien in self.aliens.sprites():
                if alien.rect.colliderect(self.ship.rect) or alien.rect.left <= 0:
                    self.game_active = False
                    self.mouse.set_visible(True)
                    self._reset_game()




    def _reset_game(self):
        self.laser.empty()
        self.aliens.empty()
        self._create_fleet()

        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_lives()

    def _create_fleet(self):
        alien = Alien(self, 0, 0)
        alien_width, alien_height = alien.rect.size


        current_y = alien_height
        increment_y = 2 * alien_height


        while current_y < self.settings.screen_height - 3 * alien_height:

            current_x = alien_width
            increment_x = 2 * alien_width

            while current_x < self.settings.screen_width - alien_width:

                alien = Alien(self, current_x, current_y)
                alien.rect.x = current_x
                alien.rect.y = current_y
                self.aliens.add(alien)

                current_x += increment_x
            current_y += increment_y


    def _update_screen(self):
        self.screen.fill((30, 30, 30))

        self.ship.blitme()
        self.aliens.draw(self.screen)

        for laser in self.laser.sprites():
            laser.draw_laser()
        if not self.game_active:
            self.play_button.draw_button()

        self.sb.show_score()
        pygame.display.flip()

        
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

           
