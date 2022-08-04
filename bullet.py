import pygame
from pygame.sprite import Sprite

# Bullet class inherits from Sprite
# Use sprites to group related elements and act on all grouped elements at once.

class Bullet(Sprite):
    """A Class to manage bullets fired from ship"""
    # To create bullent instance __init__ requires current instance of AlienInvasion
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position. """
        # call super to inherit properties from Sprite
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # Position the bullet at mid top of ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)