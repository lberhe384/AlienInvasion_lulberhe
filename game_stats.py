class GameStats:
    def __init__(self):
        self.high_score = 0
        self.reset_stats()
    def reset_stats(self):
        """Initialize stat that can change during the game."""
        self.score = 0
        self.lives = 3

        