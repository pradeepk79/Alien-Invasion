# import sys module to exit the game if user quits by closing the window.
import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        # the function initializes the background settings that Pygame needs to work properly
        pygame.init()

        """Use call set mode to create a display window"""
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # import ship and create an instance of ship once the screen is created
        # Call to Ship class requires one argument, an instance of Alien Invasion,
        # self refers to current instance of Alien Invasion, gives Ship access to games resources such as screen object

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        # Game is controlled by Run Game Method
        #  while loop contains an event loop
        # and code that manages screen updates.
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # After filling the background, draw ship on the screen so ship appears on top of background

            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            pygame.display.update()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
