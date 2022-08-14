class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize stastics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an In active state.
        self.game_active = False
        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize stastics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        # To reset the score each time a new game starts
        self.score = 0
        # To display players level in the game
        self.level = 1




