# import sys module to exit the game if user quits by closing the window.
import sys

import pygame


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        # the function initializes the background settings that Pygame needs to work properly
        pygame.init()

        """Use call set mode to create a display window"""

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set background color.
        self.bg_color = (230,230,230)

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
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
