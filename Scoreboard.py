import pygame.font

class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_lives()

    def prep_score(self):
        """Turn score into rendered image."""
        score_str = f"Score: {self.stats.score}"
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        self.score_rect = self.score_image.get_rect()
        self.score_rect.topright = self.screen_rect.topright
        self.score_rect.x -= 20

    def prep_high_score(self):
        """Turn high score into rendered image."""
        high_score_str = f"High Score: {self.stats.high_score}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10

    def prep_lives(self):
        """Display lives remaining."""
        lives_str = f"Lives: {self.stats.lives}"
        self.lives_image = self.font.render(
            lives_str, True, self.text_color, self.settings.bg_color
        )

        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.topleft = self.screen_rect.topleft
        self.lives_rect.x += 20

    def show_score(self):
        """Draw all scoreboard elements."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lives_image, self.lives_rect)


