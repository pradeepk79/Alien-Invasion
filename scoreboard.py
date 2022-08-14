import pygame.font
# to create group of ships, import Group and Ship classes.
from pygame.sprite import Group

from ship import  Ship

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize score keeping attributes"""
        # Assign game's instance to an attribute to create some ships
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None,48)

        # Prepare the initial score image.
        self.prep_score()

        # To display high score image separately from regular score.
        self.prep_high_score()

        # To display the current level
        self.prep_level()

        # To create ships
        self.prep_ships()

    # To turn text to be displayed into an image
    def prep_score(self):
        """Turn the score into a rendered image"""
        # Report scores as multiples of 10
        # Negative number as second argument in round() function rounds to nearest 10,100,1000
        rounded_score = round(self.stats.score, -1)
        # To insert commas into numbers whrn converting numerical value to string
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    # To prepare high score image
    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        # Round the highest score to nearest 10 and format with commas
        high_score = round(self.stats.high_score, -1)
        # Foramt high score  with commas
        high_score_str = "{:,}".format(high_score)
        # Generate image from high score
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

     # To display the rendered score image
    def show_score(self):
        """Draw score, level, and ships  to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    # Method to check for high scores
    def check_high_score(self):
        """Check to see if there's a new high score. """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        # Create an empty group self.ships to hold ship instances
        self.ships = Group()
        # A loop runs for every ship the player is left with
        for ship_number in range(self.stats.ships_left):
            # Create a new ship
            ship = Ship(self.ai_game)
            # Set each ships x coordinate value so ships appear next to each other
            # with 10 pixel margin on left side of group of ships
            ship.rect.x = 10 + ship_number * ship.rect.width
            # Set y coordinate from top down of the screen
            ship.rect.y = 10
            self.ships.add(ship)